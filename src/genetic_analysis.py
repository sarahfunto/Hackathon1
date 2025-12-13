"""
Basic data loading, cleaning and risk recommendation functions
for the Genetictac Hackathon Project.
"""

from typing import Tuple
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load the CSV dataset."""
    try:
        genetic = pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: file not found → {path}")
    return genetic


def clean_data(genetic: pd.DataFrame) -> pd.DataFrame:
    """Clean and encode categorical values into numeric format."""
    genetic_clean = genetic.copy()

    # Strip whitespace
    genetic_clean = genetic_clean.applymap(lambda x: x.strip() if isinstance(x, str) else x)

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
        if col in genetic_clean.columns:
            genetic_clean[col] = genetic_clean[col].map(binary_mapping)

    # Apply risk mapping
    if "Environmental Risk Exposure" in genetic_clean.columns:
        genetic_clean["Environmental Risk Exposure"] = genetic_clean["Environmental Risk Exposure"].map(risk_mapping)

    return genetic_clean


def add_recommendations(genetic: pd.DataFrame) -> pd.DataFrame:
    """Add a simple rule-based risk recommendation."""
    genetic = genetic.copy()

    def risk(row):
        if (row["Parental History"] == 1 or row["Sibling History"] == 1) and row["Environmental Risk Exposure"] == 2:
            return "High risk: recommend genetic testing"
        elif (row["Parental History"] == 1 or row["Sibling History"] == 1):
            return "Moderate risk: monitor patient"
        else:
            return "Low risk: standard follow-up"

    genetic["Recommendation"] = genetic.apply(risk, axis=1)
    return genetic


def main() -> None:
    """Run a minimal example."""
    genetic = load_data("data/family_history_rare_disease_cleaned.csv")
    genetic_clean = clean_data(genetic)
    genetic_rec = add_recommendations(genetic_clean)
    print(genetic_rec.head())


if __name__ == "__main__":
    main()
