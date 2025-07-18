"""
create_folders.py

This script creates the full directory structure for the BRD4-BD1 ligand redocking pipeline.
It ensures that all necessary subfolders (e.g., data, ligands, docking, logs) are present
before running any data preparation or docking scripts.

Author: Chinazo Emeh
Date: 2025-07-03
"""

from pathlib import Path

# Define the base project directory (update this to your actual path)
project_dir = Path("/Users/chinazoemeh/HopeMScP")

# List of subdirectories to create within the project
folders = [
    project_dir / "data/pdb_files",# Raw downloaded PDBs
    project_dir / "data/ligands",# Raw ligand mapping CSVs
    project_dir / "data/receptors",# Cleaned receptor files
    project_dir / "data/sdf", # SDF files
    project_dir / "data/smiles",# SMILES files
    project_dir / "data/rmsd_filtered",# RMSD filtered results
    project_dir / "docking/inputs",# Docking input files
    project_dir / "docking/outputs",# Docking results
    project_dir / "docking/visualizations", # Docked ligand snapshots
    project_dir / "ligands",# Folder per ligand (.pdb + .png)
    project_dir / "ligands_pdbqt",# Central .pdbqt files for GNINA
    project_dir / "ligand_visualizations",# All extracted ligand images
    project_dir / "logs" # Log files
]

# Create each folder (including any missing parent folders)
for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

# Optional: confirm success
print("All folders created under:", project_dir.resolve())
