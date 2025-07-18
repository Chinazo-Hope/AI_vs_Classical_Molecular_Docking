"""
Script Name: extract_ligands_split_dual.py
Author: Chinazo Emeh
Date: 2025-07-17

Description:
------------
This script processes a curated Excel file named 'dual_ligand_database.xlsx' containing
both BRD4-BD2 and ACHE entries. For each entry, the script:

1. Cleans and extracts the 4-letter PDB ID (uppercase) from the 'PDB ID' column
2. Downloads the corresponding .pdb file from the RCSB Protein Data Bank
3. Parses all residues and ligands in the structure:
   - Identifies ligand candidates (HETATM records excluding common solvents)
   - Selects the most likely bound ligand (by frequency)
   - Collects all residue names for completeness
4. Separates the results based on whether the entry is BRD4-BD2 or ACHE
5. Saves results into two separate CSV files:
   - data/ligand_mapping_bd2.csv
   - data/ligand_mapping_ache.csv

Dependencies:
-------------
- pandas
- biopython
- requests

Run this on your local machine (e.g. Mac) where you have full internet access.

Outputs:
--------
- ligand_mapping_bd2.csv
- ligand_mapping_ache.csv

These files will support downstream redocking, RMSD filtering, and AI benchmarking.
"""

import pandas as pd
import requests
from Bio.PDB import PDBParser
from io import StringIO
from collections import Counter
from pathlib import Path

# ------------------- Configuration -------------------
EXCEL_FILENAME = "dual_ligand_database.xlsx"
OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_BD2 = OUTPUT_DIR / "ligand_mapping_bd2.csv"
OUTPUT_ACHE = OUTPUT_DIR / "ligand_mapping_ache.csv"
SOLVENTS = {"HOH", "WAT", "SO4", "PO4", "CL", "NA", "MG", "ZN", "K", "CA"}

# ------------------- Step 1: Load Excel -------------------
df = pd.read_excel(EXCEL_FILENAME)
df.columns = [col.strip() for col in df.columns]  # Clean column names

# Confirm required columns exist
if "Unique_ID" not in df.columns or "PDB ID" not in df.columns:
    raise ValueError("Excel must contain 'Unique_ID' and 'PDB ID' columns.")

# Extract clean 4-letter PDB IDs
df["PDB_ID"] = df["PDB ID"].str.extract(r'(\w{4})')[0].str.upper()
df = df.dropna(subset=["PDB_ID"])  # Drop rows with missing/invalid PDBs

# ------------------- Step 2: Loop through entries -------------------
bd2_results = []
ache_results = []

for idx, row in df.iterrows():
    unique_id = row["Unique_ID"]
    full_pdb_label = row["PDB ID"]
    pdb_id = row["PDB_ID"]

    # Construct the download URL
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"

    try:
        response = requests.get(url)
        response.raise_for_status()

        parser = PDBParser(QUIET=True)
        structure = parser.get_structure(pdb_id, StringIO(response.text))

        ligands = []
        all_residues = set()
        residue_counts = Counter()

        # Walk through atoms and residues
        for model in structure:
            for chain in model:
                for residue in chain:
                    resname = residue.get_resname().strip()
                    all_residues.add(resname)

                    # Ligand candidate check: HETATM but not solvent
                    if residue.id[0] != " ":
                        if resname not in SOLVENTS:
                            ligands.append(resname)
                            residue_counts[resname] += 1

        # Choose the most common ligand (by atom count)
        main_ligand = residue_counts.most_common(1)[0][0] if residue_counts else "None"
        all_ligs = ", ".join(sorted(set(ligands))) if ligands else "None"
        residues_str = ", ".join(sorted(all_residues))

        result_row = {
            "Unique_ID": unique_id,
            "PDB ID": full_pdb_label,
            "PDB_ID": pdb_id,
            "Ligand(s)": main_ligand,
            "All Ligand Candidates": all_ligs,
            "All Residues": residues_str
        }

        # Save to the right list based on Unique_ID
        if "bd2" in unique_id.lower():
            bd2_results.append(result_row)
        elif "ache" in unique_id.lower():
            ache_results.append(result_row)

    except Exception as e:
        print(f"Skipping {pdb_id} due to error: {e}")

# ------------------- Step 3: Save CSV Files -------------------
pd.DataFrame(bd2_results).to_csv(OUTPUT_BD2, index=False)
pd.DataFrame(ache_results).to_csv(OUTPUT_ACHE, index=False)

print(f"\n✅ Saved {len(bd2_results)} BD2 entries to: {OUTPUT_BD2.resolve()}")
print("\nPreview of first 10 rows (BD2):")
print(pd.DataFrame(bd2_results).head(10))

print(f"\n✅ Saved {len(ache_results)} ACHE entries to: {OUTPUT_ACHE.resolve()}")
print("\nPreview of first 10 rows (ACHE):")
print(pd.DataFrame(ache_results).head(10))
