import requests
from Bio.PDB import PDBParser
from io import StringIO
import pandas as pd
from collections import Counter

# List of 5 PDBs to test
pdb_ids = ['7RUI', '7EHW', '7EHY', '7EIG', '7REK']

# Common solvents/ions to exclude
solvents = {"HOH", "WAT", "SO4", "PO4", "CL", "NA", "MG", "ZN", "K", "CA"}

# Storage for results
results = []

# Loop through each PDB
for pdb_id in pdb_ids:
    try:
        url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
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
                        if resname not in solvents:
                            ligands.append(resname)
                            residue_counts[resname] += 1

        most_common_ligand = residue_counts.most_common(1)[0][0] if residue_counts else "None"

        results.append({
            "PDB_ID": pdb_id,
            "Ligand(s)": most_common_ligand,
            "All Ligand Candidates": ", ".join(sorted(set(ligands))) if ligands else "None",
            "All Residues": ", ".join(sorted(all_residues))
        })

    except Exception as e:
        results.append({
            "PDB_ID": pdb_id,
            "Ligand(s)": f"Error: {e}",
            "All Ligand Candidates": "N/A",
            "All Residues": "N/A"
        })

# Convert to DataFrame and show results
df = pd.DataFrame(results)
print(df)

# Optional: Save to CSV
df.to_csv("ligand_residue_test.csv", index=False)
print("\nResults saved to ligand_residue_test.csv")
