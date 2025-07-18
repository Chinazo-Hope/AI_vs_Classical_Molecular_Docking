"""
convert_ligand_single.py

This script performs a single-ligand conversion as part of a validated ligand processing pipeline.

Function:
- Converts one ligand-only `.pdb` file into:
  - `.sdf` format (for cheminformatics and 2D/3D tools)
  - `.pdbqt` format (for GNINA or AutoDock docking)

Design Considerations:
- Uses Python bindings to Open Babel (pybel) for conversion instead of shell commands
- Processes only one file, providing a reproducible and minimal working example
- Skips any ligand already processed (if `.pdbqt` exists) to avoid overwriting
- All converted outputs are suffixed with `_TEST` to preserve original datasets

Input Directory:
- data/ligands/

Output Directories:
- data/ligands_sdf/
- data/ligands_pdbqt/

Requirements:
- Open Babel with Python bindings (`openbabel`, `pybel`)
- Python 3.7+

Author: Chinazo Emeh
Date: 14 July 2025
"""

from pathlib import Path
from openbabel import openbabel
import pybel

# === Set project base path === #
project_dir = Path("/Users/chinazoemeh/HopeMScP")

# === Define input/output directories === #
ligands_dir = project_dir / "data/ligands"
sdf_output_dir = project_dir / "data/ligands_sdf"
pdbqt_output_dir = project_dir / "data/ligands_pdbqt"

# Ensure output folders exist
sdf_output_dir.mkdir(parents=True, exist_ok=True)
pdbqt_output_dir.mkdir(parents=True, exist_ok=True)

# === Locate the first ligand-only .pdb file === #
for pdb_file in ligands_dir.rglob("*.pdb"):
    # Skip test ligands or previously marked files
    if "TEST" in pdb_file.parts or "TEST" in pdb_file.name:
        continue

    base_name = pdb_file.stem                      # e.g., BRD4-BD1_1_7RUI
    test_base_name = f"{base_name}_TEST"           # e.g., BRD4-BD1_1_7RUI_TEST

    sdf_path = sdf_output_dir / f"{test_base_name}.sdf"
    pdbqt_path = pdbqt_output_dir / f"{test_base_name}.pdbqt"

    # Skip if .pdbqt already exists to avoid duplication
    if pdbqt_path.exists():
        print(f"File already exists: {pdbqt_path.name}. Skipping.")
        break

    print(f"Converting ligand: {base_name}")

    try:
        # Load the ligand from PDB
        mol = next(pybel.readfile("pdb", str(pdb_file)))

        # Add hydrogens and perform a quick 3D optimization
        mol.addh()
        mol.make3D()

        # Write to .sdf
        mol.write("sdf", str(sdf_path), overwrite=True)
        print(f".sdf file written to: {sdf_path.name}")

        # Write to .pdbqt
        mol.write("pdbqt", str(pdbqt_path), overwrite=True)
        print(f".pdbqt file written to: {pdbqt_path.name}")

    except Exception as e:
        print(f"Conversion failed for {base_name}: {e}")

    break  # Exit after processing a single ligand

print("Conversion complete.")
