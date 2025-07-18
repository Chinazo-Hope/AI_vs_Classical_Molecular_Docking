"""
extract_ligands_full.py

Author: Chinazo Emeh  
MSc Project: Learning Molecular Structure and Dynamics using Artificial Intelligence  
Date: 08 July 2025  

This script processes a curated list of protein–ligand complexes provided in an Excel file
(ligand_database.xlsx), extracting both the primary bound ligand and the full set of residue names
from each PDB file. It is designed for high-throughput ligand mapping workflows, particularly for
downstream applications such as molecular docking, redocking validation, RMSD pose filtering, and
benchmarking of AI-based docking models (e.g., GNINA, DiffDock).

For each entry in the Excel file, the script:
- Extracts the 4-letter PDB ID from the PBD ID field
- Downloads the corresponding .pdb file from the RCSB Protein Data Bank
- Parses all residues (both ATOM and HETATM records)
- Identifies ligand candidates by filtering out common solvents and crystallization agents
- Automatically selects the most prominent ligand (based on atom count)
- Records all residue names present in the structure for traceability and validation

The output is saved to: data/ligand_mapping_full.csv

Each row in the CSV contains:
- UniqueID (from the Excel sheet)
- PBD ID and cleaned 4-character PDB ID
- Most likely bound ligand
- All ligand-like HETATM entries
- Complete list of residue names (including amino acids, ligands, ions, solvents)

This script is designed for reproducibility and scalability in large-scale structure-based AI validation pipelines.
"""
import pandas as pd
import requests
from Bio.PDB import PDBParser
from io import StringIO
from collections import Counter
from pathlib import Path

# --- Configuration ---
EXCEL_FILENAME = "ligand_database.xlsx"
OUTPUT_FILENAME = "ligand_mapping_full.csv"
SOLVENTS = {"HOH", "WAT", "SO4", "PO4", "CL", "NA", "MG", "ZN", "K", "CA"}

# --- Load Excel File ---
df = pd.read_excel(EXCEL_FILENAME)
df.columns = [col.strip() for col in df.columns]
df["PBD ID"] = df["PBD ID"].astype(str).str.replace("\xa0", "", regex=False).str.strip()
df["UniqueID"] = df["UniqueID"].astype(str).str.strip()
df["PDB_ID"] = df["PBD ID"].str.extract(r'(\w{4})$')[0].str.upper().str.strip()

# --- Setup Output Path ---
output_path = Path("data") / OUTPUT_FILENAME
output_path.parent.mkdir(parents=True, exist_ok=True)

# --- Parse PDBs ---
results = []

for _, row in df.iterrows():
    pdb_id = row["PDB_ID"]
    unique_id = row["UniqueID"]
    full_pbd_id = row["PBD ID"]
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
            "PBD ID": full_pbd_id,
            "PDB_ID": pdb_id,
            "Ligand(s)": most_common_ligand,
            "All Ligand Candidates": ", ".join(sorted(set(ligands))) if ligands else "None",
            "All Residues": ", ".join(sorted(all_residues))
        })

    except Exception as e:
        print(f"Error fetching {pdb_id}: {e}")
        results.append({
            "UniqueID": unique_id,
            "PBD ID": full_pbd_id,
            "PDB_ID": pdb_id,
            "Ligand(s)": f"Error: {e}",
            "All Ligand Candidates": "N/A",
            "All Residues": "N/A"
        })

# --- Save Output ---
final_df = pd.DataFrame(results)
final_df.to_csv(output_path, index=False)

print(f"\n✅ All data saved to {output_path.resolve()}")
print("\nPreview of first 10 rows:")
print(final_df.head(10))
