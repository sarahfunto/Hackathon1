"""
Basic data loading, cleaning and risk recommendation functions
for the Genetictac Hackathon Project.
"""

from typing import Tuple
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load the CSV dataset."""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: file not found → {path}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and encode categorical values into numeric format."""
    df_clean = df.copy()

    # Strip whitespace
    df_clean = df_clean.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Binary mapping
    binary_mapping = {
        "Yes": 1, "No": 0,
        "Y": 1, "N": 0,
        "P": 1,
        "Male": 1, "Female": 0, "Other": 2
    }

    # Multi-category mapping
    risk_mapping = {"Low": 0, "Moderate": 1, "High": 2}

    # Apply binary mapping
    binary_columns = [
        "Parental History", "Sibling History", "Known Genetic Mutation",
        "Early Onset Cases in Family", "geneticTest", "Gender"
    ]

    for col in binary_columns:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].map(binary_mapping)

    # Apply risk mapping
    if "Environmental Risk Exposure" in df_clean.columns:
        df_clean["Environmental Risk Exposure"] = df_clean["Environmental Risk Exposure"].map(risk_mapping)

    return df_clean


def add_recommendations(df: pd.DataFrame) -> pd.DataFrame:
    """Add a simple rule-based risk recommendation."""
    df = df.copy()

    def risk(row):
        if (row["Parental History"] == 1 or row["Sibling History"] == 1) and row["Environmental Risk Exposure"] == 2:
            return "High risk: recommend genetic testing"
        elif (row["Parental History"] == 1 or row["Sibling History"] == 1):
            return "Moderate risk: monitor patient"
        else:
            return "Low risk: standard follow-up"

    df["Recommendation"] = df.apply(risk, axis=1)
    return df


def main() -> None:
    """Run a minimal example."""
    df = load_data("data/family_history_rare_disease_cleaned.csv")
    df_clean = clean_data(df)
    df_rec = add_recommendations(df_clean)
    print(df_rec.head())


if __name__ == "__main__":
    main()
