"""
Basic data loading, cleaning and risk recommendation functions
for the Genetictac Hackathon Project.
"""

from typing import Dict
import pandas as pd
from scipy.stats import chi2_contingency


def load_genetic_data(filepath: str) -> pd.DataFrame:
    """Load the CSV dataset."""
    try:
        genetic = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: file not found → {filepath}")
    return genetic


def clean_data(genetic: pd.DataFrame) -> pd.DataFrame:
    """Clean and encode categorical values into numeric format."""
    genetic_clean = genetic.copy()

    # Strip whitespace
    genetic_clean = genetic_clean.applymap(
        lambda x: x.strip() if isinstance(x, str) else x
    )

    # Binary mapping
    binary_mapping = {
        "Yes": 1, "No": 0,
        "Y": 1, "N": 0,
        "P": 1,
        "Male": 1, "Female": 0, "Other": 2,
    }

    risk_mapping = {"Low": 0, "Moderate": 1, "High": 2}

    binary_columns = [
        "Parental History", "Sibling History", "Known Genetic Mutation",
        "Early Onset Cases in Family", "geneticTest", "Gender",
    ]

    for col in binary_columns:
        if col in genetic_clean.columns:
            genetic_clean[col] = genetic_clean[col].map(binary_mapping)

    if "Environmental Risk Exposure" in genetic_clean.columns:
        genetic_clean["Environmental Risk Exposure"] = (
            genetic_clean["Environmental Risk Exposure"].map(risk_mapping)
        )

    return genetic_clean


def run_chi_squared(df: pd.DataFrame, var1: str, var2: str) -> Dict[str, float]:
    """Run chi-squared test between two categorical variables."""
    contingency = pd.crosstab(df[var1], df[var2])
    chi2, p, dof, expected = chi2_contingency(contingency)
    return {
        "chi2": float(chi2),
        "p_value": float(p),
        "dof": int(dof),
        "significant": bool(p < 0.05),
    }


def calculate_risk(row: pd.Series) -> str:
    """Calculate patient risk level based on family history and environment."""
    if (
        row["Parental History"] == 1
        or row["Sibling History"] == 1
    ) and row["Environmental Risk Exposure"] == 2:
        return "High risk: recommend genetic testing"
    elif row["Parental History"] == 1 or row["Sibling History"] == 1:
        return "Moderate risk: monitor patient"
    else:
        return "Low risk: standard follow-up"


def add_recommendations(genetic: pd.DataFrame) -> pd.DataFrame:
    """Add a simple rule-based risk recommendation."""
    genetic = genetic.copy()
    genetic["Recommendation"] = genetic.apply(calculate_risk, axis=1)
    return genetic


def main() -> None:
    """Run a minimal example."""
    genetic = load_genetic_data("data/family_history_rare_disease_cleaned.csv")
    genetic_clean_

