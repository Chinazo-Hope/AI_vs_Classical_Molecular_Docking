"""
Script Name: extract_ligands_dual_cleaned.py
Author: Chinazo Emeh
Date: 2025-07-17

Description:
------------
This script processes two sheets from a dual Excel file containing curated 
lists of protein–ligand complexes for AChE and BRD4-BD2.

For each PDB ID in the sheets:
- Downloads the PDB file from RCSB
- Extracts all unique residues
- Identifies potential ligands (non-solvent HETATM residues)
- Selects the most common ligand (by atom count)
- Drops any entries where ligand extraction failed (ligand = 'None' or 'N/A')

Outputs:
- Saves one CSV for AChE and one for BD2 into the `data/` folder
- Prints number of successful extractions for each protein type

Dependencies:
    pip install pandas requests biopython openpyxl

Input:
    - dual_ligand_database.xlsx
        ├── Sheet: AChE
        ├── Sheet: BD2

Output:
    - data/ligand_mapping_ache_cleaned.csv
    - data/ligand_mapping_bd2_cleaned.csv
"""

import pandas as pd
import requests
from Bio.PDB import PDBParser
from io import StringIO
from collections import Counter
from pathlib import Path

# ------------------ CONFIG ------------------

EXCEL_FILE = "dual_ligand_database.xlsx"
SHEETS = {"AChE": "ligand_mapping_ache_cleaned.csv", 
          "BD2": "ligand_mapping_bd2_cleaned.csv"}
SOLVENTS = {"HOH", "WAT", "SO4", "PO4", "CL", "NA", "MG", "ZN", "K", "CA"}

# Create data/ directory if it doesn't exist
Path("data").mkdir(parents=True, exist_ok=True)

# ------------------ MAIN ------------------

for sheet_name, output_file in SHEETS.items():
    print(f"\n🔍 Processing sheet: {sheet_name}")
    
    df = pd.read_excel(EXCEL_FILE, sheet_name=sheet_name)

    # Clean up column names
    df.columns = [col.strip() for col in df.columns]
    
    # Sanitize and extract clean 4-letter PDB codes
    df["PDB ID"] = df["PDB ID"].astype(str).str.strip().str.upper()
    df["PDB_ID"] = df["PDB ID"].str.extract(r'(\w{4})$')[0].str.upper()

    results = []

    for _, row in df.iterrows():
        unique_id = row["Unique_ID"]
        full_pbd_id = row["PDB ID"]
        pdb_id = row["PDB_ID"]
        pdb_url = f"https://files.rcsb.org/download/{pdb_id}.pdb"

        try:
            # Download and parse the PDB file
            response = requests.get(pdb_url)
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

                        # Only consider HETATM residues that aren't solvents
                        if residue.id[0] != " " and resname not in SOLVENTS:
                            ligands.append(resname)
                            residue_counts[resname] += 1

            # Choose most common ligand or default to "None"
            most_common_ligand = residue_counts.most_common(1)[0][0] if residue_counts else "None"

            results.append({
                "UniqueID": unique_id,
                "PBD ID": full_pbd_id,
                "PDB_ID": pdb_id,
                "Ligand(s)": most_common_ligand,
                "All Ligand Candidates": ", ".join(sorted(set(ligands))) if ligands else "None",
                "All Residues": ", ".join(sorted(all_residues)) if all_residues else "None"
            })

        except Exception as e:
            print(f"Skipping {pdb_id} due to error: {e}")
            results.append({
                "UniqueID": unique_id,
                "PBD ID": full_pbd_id,
                "PDB_ID": pdb_id,
                "Ligand(s)": "N/A",
                "All Ligand Candidates": "N/A",
                "All Residues": "N/A"
            })

    # Convert results to DataFrame
    result_df = pd.DataFrame(results)

    # Drop entries with failed ligand extraction
    result_df = result_df[result_df["Ligand(s)"].isin(["None", "N/A"]) == False]

    # Save to CSV
    output_path = Path("data") / output_file
    result_df.to_csv(output_path, index=False)

    print(f"✅ Saved {len(result_df)} cleaned entries to: {output_path.resolve()}")
    print(f"\nPreview of first 10 rows ({sheet_name}):")
    print(result_df.head(10))
