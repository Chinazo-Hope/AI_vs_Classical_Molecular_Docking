"""
ligand_mapping.py

This script loads BRD4-BD1 metadata from Excel, extracts PDB_IDs and ligand residue names
from downloaded PDB structures, and saves the mapping to CSV for use in downstream processing.

Author: Chinazo Emeh
Date: 2025-07-03
"""

import pandas as pd
from pathlib import Path

# Step 1: Define paths
project_dir = Path.cwd()
excel_file = project_dir / "ligand_database.xlsx"
sheet_name = "BRD4-BD1(PDB)"
pdb_dir = project_dir / "data" / "pdb_files"
output_csv = project_dir / "data" / "ligand_mapping.csv"

# Step 2: Load Excel file
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Step 3: Clean and extract key columns
df = df.rename(columns={"Unique ID Number": "UniqueID"})
df["PDB_ID"] = df["PBD ID"].str.extract(r'([0-9a-zA-Z]{4})$', expand=False).str.upper()
df["Ligand_Resname"] = None  # Placeholder for ligand residue names

# Step 4: Scan each PDB file for ligand resname (exclude solvents and common ions)
exclude_resnames = {"HOH", "SO4", "PO4", "CL", "NA", "MG", "CA", "ZN", "K"}

for idx, row in df.iterrows():
    pdb_id = row["PDB_ID"]
    pdb_path = pdb_dir / f"{pdb_id}.pdb"

    if not pdb_path.exists():
        print(f"[{pdb_id}] File not found: {pdb_path.name}")
        continue

    ligands = set()
    with open(pdb_path, "r") as f:
        for line in f:
            if line.startswith("HETATM"):
                resname = line[17:20].strip()
                if resname and resname.upper() not in exclude_resnames:
                    ligands.add(resname)

    if len(ligands) == 1:
        df.at[idx, "Ligand_Resname"] = list(ligands)[0]
    elif len(ligands) > 1:
        df.at[idx, "Ligand_Resname"] = ";".join(sorted(ligands))
        print(f"[{pdb_id}] Multiple ligands found: {ligands}")
    else:
        print(f"[{pdb_id}]  No ligand detected.")

# Step 5: Save the DataFrame as CSV
output_csv.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_csv, index=False)

# Step 6: Preview output
print("\n ligand_mapping.csv created. Preview:")
print(df.head(10))

