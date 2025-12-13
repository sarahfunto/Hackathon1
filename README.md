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

  File: family_history_rare_disease_cleaned.csv
  1,000 rows, 10 columns (Age, Gender, Parental History, Sibling History, Number of Relatives with Disease, Known Genetic Mutation, Environmental Risk Exposure, geneticTest, etc.)

Tech stack

  Python 3
  NumPy
  pandas
  seaborn & matplotlib
  SciPy

How to run :  Google Colab (recommended)

  Open the notebook: genetic_analysis.ipynb in Google Colab.
  Upload family_history_rare_disease_cleaned.csv in the same session.
  Click Run all → the plots, tests and recommendations will appear.

🎥 Demo video : https://youtu.be/HrJ5fSMa5GI

Short Summary 

This project analyzes a synthetic dataset of 1,000 patients with a possible rare genetic disease.
It explores basic factors such as family history, genetic mutations, and environmental risk, and then uses a simple rule-based system to assign each patient a risk level:
Low risk – standard follow-up
Moderate risk – monitor the patient
High risk – recommend genetic testing
The notebook also performs basic data cleaning, visualizations, and simple statistical tests to understand how these variables are related.
This is a beginner-friendly project created for a hackathon to demonstrate how data can support decision making in a medical context (not for clinical use).
