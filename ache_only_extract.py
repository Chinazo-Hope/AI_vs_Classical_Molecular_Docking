"""
Script Name: extract_ligands_ache.py
Author: Chinazo Emeh
Date: 17 July 2025

Description:
------------
This script reads the 'AChE' sheet from a dual Excel file that contains protein-ligand information.
For each entry in the sheet, it:
- Cleans the 'PDB ID' column (removes extra spaces, extracts last 4 chars, converts to uppercase)
- Downloads the corresponding PDB file from RCSB
- Parses the structure to:
    • Extract all residue names (ATOM + HETATM)
    • Filter out common solvents/ions
    • Identify all ligand-like molecules (non-solvent HETATM)
    • Determine the most prominent ligand (based on atom count)

The results are saved to a CSV file:
    data/ligand_mapping_ache.csv

Dependencies:
    pip install pandas biopython requests
"""

import pandas as pd
import requests
from Bio.PDB import PDBParser
from io import StringIO
from collections import Counter
from pathlib import Path

# --- Config ---
EXCEL_PATH = "dual_ligand_database.xlsx"
SHEET_NAME = "AChE"
OUTPUT_PATH = Path("data/ligand_mapping_ache.csv")
SOLVENTS = {"HOH", "WAT", "SO4", "PO4", "CL", "NA", "MG", "ZN", "K", "CA"}

# --- Load and clean Excel data ---
df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)
df.columns = [col.strip() for col in df.columns]
df["PDB ID"] = df["PDB ID"].astype(str).str.replace("\xa0", "", regex=False).str.strip()
df["PDB_ID"] = df["PDB ID"].str.extract(r'(\w{4})$')[0].str.upper().str.strip()
df["Unique_ID"] = df["Unique_ID"].astype(str).str.strip()

# --- Setup output ---
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
results = []

# --- Process each row ---
for _, row in df.iterrows():
    pdb_id = row["PDB_ID"]
    unique_id = row["Unique_ID"]
    original_pbd_id = row["PDB ID"]
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"

    try:
        response = requests.get(url)
        response.raise_for_status()

        parser = PDBParser(QUIET=True)
        structure = parser.get_structure(pdb_id, StringIO(response.text))

        ligands = []
        all_residues = set()
        residue_counts = Counter()

        for model in structure:
            for chain in model:
                for residue in chain:
                    resname = residue.get_resname().strip()
                    all_residues.add(resname)

                    if residue.id[0] != " ":  # HETATM
                        if resname not in SOLVENTS:
                            ligands.append(resname)
                            residue_counts[resname] += 1

        most_common_ligand = residue_counts.most_common(1)[0][0] if residue_counts else "None"

        results.append({
            "UniqueID": unique_id,
            "PBD ID": original_pbd_id,
            "PDB_ID": pdb_id,
            "Ligand(s)": most_common_ligand,
            "All Ligand Candidates": ", ".join(sorted(set(ligands))) if ligands else "None",
            "All Residues": ", ".join(sorted(all_residues))
        })

    except Exception as e:
        print(f"Skipping {pdb_id} due to error: {e}")
        continue

# --- Save CSV ---
final_df = pd.DataFrame(results)
final_df.to_csv(OUTPUT_PATH, index=False)

print(f"\n✅ Saved {len(final_df)} entries to: {OUTPUT_PATH.resolve()}")
print("\nPreview of first 10 rows (ACHE):")
print(final_df.head(10))
