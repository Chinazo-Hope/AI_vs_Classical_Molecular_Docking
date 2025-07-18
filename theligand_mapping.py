import requests
from Bio.PDB import PDBParser
from io import StringIO
import pandas as pd

# Set the PDB ID to test
pdb_id = '7RUI'
url = f'https://files.rcsb.org/download/{pdb_id}.pdb'

# Solvent exclusion list
solvents = {"HOH", "WAT", "SO4", "PO4", "CL", "NA", "MG", "ZN", "K", "CA"}

# Download and parse PDB
response = requests.get(url)
response.raise_for_status()

parser = PDBParser(QUIET=True)
structure = parser.get_structure(pdb_id, StringIO(response.text))

# Extract residues
ligands = set()
all_residues = set()

for model in structure:
    for chain in model:
        for residue in chain:
            resname = residue.get_resname().strip()
            all_residues.add(resname)

            hetfield = residue.id[0]
            if hetfield.startswith("H_") or hetfield != " ":
                if resname not in solvents:
                    ligands.add(resname)

# Show result
row = {
    "PDB_ID": pdb_id,
    "Ligand(s)": ", ".join(sorted(ligands)) if ligands else "None",
    "All Residues": ", ".join(sorted(all_residues))
}

df = pd.DataFrame([row])
print(df)
