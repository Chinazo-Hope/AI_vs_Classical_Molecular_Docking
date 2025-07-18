"""
ligand_mapping.py

This script extracts key mapping information (Unique ID, PDB ID, Ligand Resname)
from an Excel file and saves it as a CSV file for use in later steps of the docking pipeline.

Author: Chinazo Emeh
Date: 2025-07-03
"""

import pandas as pd
from pathlib import Path

# Step 1: Define paths
project_dir = Path.cwd()

excel_file = project_dir / "ligand_database.xlsx"

sheet_name = "BRD4-BD1(PDB)"

data_dir = project_dir / "data"

data_dir.mkdir(exist_ok=True)

# Step 2: Load Excel file
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Step 3: Clean and prepare columns
df = df.rename(columns={"Unique ID Number": "UniqueID"})
df["PDB_ID"] = df["PBD ID"].str.extract(r'([0-9a-zA-Z]{4})$', expand=False).str.upper()

# Step 4: Add ligand resnames manually for the first 3 ligands
df.loc[0, "Ligand_Resname"] = "I01"  # 7RUI
df.loc[1, "Ligand_Resname"] = "UNL"  # 8B96
df.loc[2, "Ligand_Resname"] = "JQ1"  # 8B98

# Step 5: Save as CSV
csv_path = data_dir / "ligand_mapping.csv"
df.to_csv(csv_path, index=False)

print(f"ligand_mapping.csv saved to: {csv_path.resolve()}")
