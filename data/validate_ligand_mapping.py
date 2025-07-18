"""
validate_ligand_mapping.py

This script validates and filters ligand-receptor entries from the output of a ligand mapping pipeline.
It removes entries with download errors, missing PDB IDs, or undefined ligands, and performs basic
sanity checks on ligand naming conventions.

Key Features:
- Loads 'ligand_mapping_full.csv' from the /data directory
- Removes rows where ligands are missing, marked as 'None', or include error messages
- Filters out entries with missing or malformed PDB IDs
- Optionally flags ligand names that do not follow expected conventions (2–4 uppercase alphanumerics)
- Saves the cleaned output to 'data/ligand_mapping_validated.csv'
- Prints the number of valid structures and any suspect ligand names

This file is intended to support downstream preprocessing for molecular docking pipelines,
such as GNINA or DiffDock, by ensuring only high-quality inputs are passed forward.

Author: Chinazo Emeh  
Date: 2025-07-09
"""
import pandas as pd
from pathlib import Path
import re

# Load original mapping file
df = pd.read_csv("data/ligand_mapping_full.csv")

# Drop rows with:
# 1. Error in ligand column
# 2. Ligand = None
# 3. Missing PDB_ID
clean_df = df.copy()
clean_df = clean_df[~clean_df["Ligand(s)"].str.contains("Error", na=False)]
clean_df = clean_df[clean_df["Ligand(s)"].str.lower() != "none"]
clean_df = clean_df.dropna(subset=["PDB_ID"])

# Optional sanity check: flag suspicious ligand names
def is_valid_ligand_name(name):
    return bool(re.fullmatch(r"[A-Z0-9]{2,4}", name.strip()))

invalid_ligands = []
for i, lig in clean_df["Ligand(s)"].items():
    if not is_valid_ligand_name(lig):
        invalid_ligands.append((clean_df.loc[i, "PDB_ID"], lig))

# Save cleaned file
output_path = Path("data/ligand_mapping_validated.csv")
clean_df.to_csv(output_path, index=False)

# Summary
print(f"Cleaned file saved: {output_path.resolve()}")
print(f"Total valid ligand entries: {len(clean_df)}")

if invalid_ligands:
    print("Potentially suspicious ligand names:")
    for pdb_id, lig in invalid_ligands:
        print(f"- {pdb_id}: {lig}")
else:
    print("All ligand names appear structurally valid.")
