🧬 Genetictac – Rare Disease Family History Explorer

A simple project to explore family history of a rare disease and suggest basic risk levels for patients.

🔍 What is this project?

   This project uses a synthetic dataset of 1,000 patients to:
   Look at family history (parents, siblings, number of relatives with the disease)
   Check known genetic mutations
   Look at environmental risk exposure (Low / Moderate / High)
   See who has done a genetic test
   Then it creates a very simple rule-based recommendation:
       Low risk: standard follow-up
       Moderate risk: monitor patient
       High risk: recommend genetic testing

Dataset

  The dataset used in this project is stored in: data/family_history_rare_disease_cleaned.csv
  1,000 rows, 10 columns (Age, Gender, Parental History, Sibling History, Number of Relatives with Disease, Known Genetic Mutation, Environmental Risk Exposure, geneticTest, etc.)

Tech stack

  Python 3
  NumPy
  pandas
  seaborn & matplotlib
  SciPy
  
Clone the repository and install dependencies:
   pip install -r requirements.txt
Ensure the dataset is located in:
   data/family_history_rare_disease_cleaned.csv
   
How to run :  Google Colab 

   Open the notebook Hackaton1_en_basic.ipynb in Colab.
   Ensure the dataset is placed in data/.
   Click Run all to generate plots, tests, and recommendations.

🎥 Demo video : https://youtu.be/HrJ5fSMa5GI

Short Summary 

This project analyzes a synthetic dataset of 1,000 patients with potential rare genetic disease risk factors.
It performs data cleaning, descriptive statistics, visualizations, chi-squared tests, t-tests, and ANOVA.
It also generates a simple, interpretable rule-based recommendation for patient risk.

This project was created for a hackathon to demonstrate how data analysis can support medical decision-making (educational use only).
