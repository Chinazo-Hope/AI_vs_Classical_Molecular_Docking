"""
convert_ligands.py

DESCRIPTION:
-----------
This script automates the conversion of ligand-only .pdb files into two widely used formats:
1. .sdf – for cheminformatics applications such as molecular visualization, descriptor calculation, and compound libraries.
2. .pdbqt – for use in molecular docking tools such as GNINA and AutoDock.

It performs the following tasks:
- Recursively scans the 'data/ligands/' directory for all .pdb files associated with extracted ligands.
- Excludes any ligand files that are in folders or filenames containing the keyword 'TEST'.
- Converts each .pdb to .sdf (if enabled) and saves it to the pre-existing 'data/ligands_sdf/' directory.
- Converts each .pdb to .pdbqt (if enabled) and saves it to the new or existing 'data/ligands_pdbqt/' directory.

NOTES:
------
- The script uses Open Babel (obabel) for all format conversions, so it must be installed and accessible via your PATH.
- The output directories are organized by format and kept flat (not nested per ligand).
- Conversion options can be toggled using the boolean flags: convert_to_sdf and convert_to_pdbqt.

Author: Chinazo Emeh
Date: 14 July 2025
"""
import openbabel
import subprocess
from pathlib import Path
import glob

# === SETUP PROJECT PATHS === #
project_dir = Path("/Users/chinazoemeh/HopeMScP")

# Directory containing all ligand folders (each containing a .pdb)
ligands_dir = project_dir / "data/ligands"

# Central output folders for converted files
sdf_output_dir = project_dir / "data/ligands_sdf"        # Already exists
pdbqt_output_dir = project_dir / "data/ligands_pdbqt"    # Will be created if missing

# Ensure the pdbqt output directory exists
pdbqt_output_dir.mkdir(parents=True, exist_ok=True)

# === CONVERSION FLAGS === #
convert_to_sdf = True
convert_to_pdbqt = True

# === GLOB PATTERN: Find all .pdb files in ligand subfolders === #
# We use glob.glob here instead of pathlib.rglob for user request
# '**/*.pdb' means recursively search all folders under 'ligands/' for .pdb files
all_pdb_files = glob.glob(str(ligands_dir / '**' / '*.pdb'), recursive=True)

# === MAIN LOOP: Process each ligand file === #
for pdb_file_str in all_pdb_files:
    pdb_file = Path(pdb_file_str)

    # Skip files in 'TEST' folders or with 'TEST' in filename
    if "TEST" in pdb_file.name or any("TEST" in part for part in pdb_file.parts):
        continue

    # Extract the base name for this ligand (e.g., BRD4-BD1_1_7RUI from the filename)
    base_name = pdb_file.stem

    # Define full output paths for both formats
    sdf_path = sdf_output_dir / f"{base_name}.sdf"
    pdbqt_path = pdbqt_output_dir / f"{base_name}.pdbqt"

    # === Convert to .sdf format === #
    if convert_to_sdf:
        print(f"Converting to .sdf: {base_name}")
        subprocess.run(["obabel", str(pdb_file), "-O", str(sdf_path)], check=True)

    # === Convert to .pdbqt format === #
    if convert_to_pdbqt:
        print(f"Converting to .pdbqt: {base_name}")
        subprocess.run(["obabel", str(pdb_file), "-O", str(pdbqt_path)], check=True)

# === Final confirmation === #
print("All requested ligand files have been successfully converted.")
