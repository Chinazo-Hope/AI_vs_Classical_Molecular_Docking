"""
Script Name: bd2_only_extract.py
Author: Chinazo Emeh
Date: 2025-07-17

Description:
------------
This script processes the 'BD2' sheet from a multi-sheet Excel file (dual_ligand_database.xlsx).
It extracts ligand and residue information for BRD4-BD2 entries from the PDB and saves the results
to a structured CSV.

Output: data/ligand_mapping_bd2.csv
"""

import pandas as pd
import requests
from Bio.PDB import PDBParser
from io import StringIO
from collections import Counter
from pathlib import Path

# --- Configuration ---
EXCEL_FILENAME = "dual_ligand_database.xlsx"
SHEET_NAME = "BD2"
OUTPUT_FILENAME = "ligand_mapping_bd2.csv"
SOLVENTS = {"HOH", "WAT", "SO4", "PO4", "CL", "NA", "MG", "ZN", "K", "CA"}

# --- Load 'BD2' Sheet ---
df = pd.read_excel(EXCEL_FILENAME, sheet_name=SHEET_NAME)
df.columns = [col.strip() for col in df.columns]
df["PDB ID"] = df["PDB ID"].astype(str).str.replace("\xa0", "", regex=False).str.strip()
df["Unique_ID"] = df["Unique_ID"].astype(str).str.strip()
df["PDB_ID"] = df["PDB ID"].str.extract(r'(\w{4})$')[0].str.upper().str.strip()

# --- Setup Output Path ---
output_path = Path("data") / OUTPUT_FILENAME
output_path.parent.mkdir(parents=True, exist_ok=True)

# --- Parse PDBs ---
results = []

for _, row in df.iterrows():
    pdb_id = row["PDB_ID"]
    unique_id = row["Unique_ID"]
    full_pbd_id = row["PDB ID"]
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

                    if residue.id[0] != " ":  # HETATM record
                        if resname not in SOLVENTS:
                            ligands.append(resname)
                            residue_counts[resname] += 1

        most_common_ligand = residue_counts.most_common(1)[0][0] if residue_counts else "None"

        results.append({
            "UniqueID": unique_id,
            "PBD ID": full_pbd_id,
            "PDB_ID": pdb_id,
            "Ligand(s)": most_common_ligand,
            "All Ligand Candidates": ", ".join(sorted(set(ligands))) if ligands else "None",
            "All Residues": ", ".join(sorted(all_residues))
        })

    except Exception as e:
        print(f"Skipping {pdb_id} due to error: {e}")
        continue

# --- Save Output ---
final_df = pd.DataFrame(results)
final_df.to_csv(output_path, index=False)

print(f"\nSaved {len(final_df)} entries to: {output_path.resolve()}")
print("\nPreview of first 10 rows (BD2):")
print(final_df.head(10))
