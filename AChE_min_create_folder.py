"""
create_ache_ligand_folders_minimal.py

This script creates only the essential folder structure required to begin working
with AChE (Acetylcholinesterase) ligand files in a redocking or virtual screening pipeline.

It is intended to be used during the early phases of project setup to allow
the user to focus on immediate ligand extraction and visualisation tasks 
before setting up the full AChE docking/data workflow.

The following directories are created:

1. ligands/ache/ - stores ligand-specific subfolders (e.g., AChE_1_1EVE/) with .pdb and .png files
2. ligands_pdbqt/ache/ - holds converted ligand .pdbqt files ready for GNINA or AutoDock
3. ligand_visualizations/ache/ - stores rendered images (.png) of AChE ligands for QC and presentation

This script does not interfere with BRD4-BD1 folders or full pipeline directories.
It can be run multiple times without overwriting existing folders.

Author: Chinazo Emeh  
Date: 15/07/2025
"""

from pathlib import Path

# === Define the project base directory ===
project_dir = Path("/Users/chinazoemeh/HopeMScP")

# === List of minimal AChE-specific folders to create ===
essential_folders = [
    project_dir / "ligands" / "ache",                 # Where ligand folders (AChE_1_XXXX) will go
    project_dir / "ligands_pdbqt" / "ache",           # Converted .pdbqt files used for docking
    project_dir / "ligand_visualizations" / "ache"    # .png snapshots of ligands (rendered in VMD/PyMOL)
]

# === Create each folder, ensuring no errors if it already exists ===
for folder in essential_folders:
    folder.mkdir(parents=True, exist_ok=True)

# === Output a success message to confirm the folders were created ===
print("Created minimal AChE folders:")
for f in essential_folders:
    print("   -", f.relative_to(project_dir))
