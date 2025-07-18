"""
Script to extract and visualize a single ligand from a protein-ligand complex using VMD.

Overview:
This script automates the extraction of a ligand (identified by its residue name) from 
a protein-ligand complex PDB file using VMD (Visual Molecular Dynamics). It also 
generates a PNG image snapshot of the extracted ligand structure for visualization 
and verification.

Functionality:
1. Loads the specified PDB file from the protein-ligand complex.
2. Selects atoms corresponding to the ligand residue using a VMD atom selection query.
3. Writes a new PDB file containing only the ligand atoms.
4. Generates a high-quality PNG snapshot of the ligand using VMD’s rendering engine.

Inputs:
- A protein-ligand PDB file (.pdb) stored in data/pdb_files/
- The residue name (resname) of the ligand of interest
- A unique identifier to label output files and directories

Outputs:
- A PDB file of the extracted ligand: data/ligands/<unique_id>/<unique_id>.pdb
- A rendered PNG image of the ligand: data/ligands/<unique_id>/<unique_id>.png

Requirements:
- VMD must be installed and callable via the command line (e.g., 'vmd').
- The input PDB file must contain the specified ligand with a correct residue name.
- Paths and environment should reflect your local project directory structure.

Author:
Chinazo Emeh, MSc Computational Chemistry & Data Science
University of Strathclyde, 2025

Date:
July 2025
"""

import subprocess
from pathlib import Path

# === CONFIGURATION === #
unique_id = "BRD4-BD1_1_7RUI"         # Descriptive name for the ligand structure
pdb_filename = "7RUI.pdb"             # Full protein-ligand complex PDB file
ligand_resname = "7QZ"                # Ligand residue name (from original PDB)

# === PATH SETUP === #
project_dir = Path("/Users/chinazoemeh/HopeMScP")
input_pdb_dir = project_dir / "data/pdb_files"
output_folder = project_dir / "data/ligands" / unique_id
output_folder.mkdir(parents=True, exist_ok=True)

pdb_path = input_pdb_dir / pdb_filename
ligand_only_path = output_folder / f"{unique_id}.pdb"
snapshot_path = output_folder / f"{unique_id}.png"

# === TCL SCRIPT TO EXTRACT LIGAND === #
vmd_extract_script = f"""
mol new {pdb_path}
set sel [atomselect top "resname {ligand_resname}"]
$sel writepdb {ligand_only_path}
quit
"""

extract_tcl_path = output_folder / "extract_ligand.tcl"
extract_tcl_path.write_text(vmd_extract_script)

# === TCL SCRIPT TO RENDER LIGAND SNAPSHOT === #
render_script = f"""
mol new {ligand_only_path}
display projection orthographic
color Display Background white
render Tachyon {snapshot_path}
quit
"""

render_tcl_path = output_folder / "render.tcl"
render_tcl_path.write_text(render_script)

# === RUN VMD FOR EXTRACTION === #
print(f"Extracting ligand from {pdb_filename}...")
#subprocess.run(["vmd", "-dispdev", "text", "-e", str(extract_tcl_path)], check=True)


# === VMD EXECUTABLE PATH === #
vmd_path = "/Applications/VMD 1.9.4a57-arm64-Rev12.app/Contents/vmd/vmd_MACOSXARM64"

# === RUN VMD FOR EXTRACTION === #
print(f"Extracting ligand from {pdb_filename}...")
subprocess.run([vmd_path, "-dispdev", "text", "-e", str(extract_tcl_path)], check=True)

# === RUN VMD FOR VISUALIZATION === #
print(f"Rendering PNG snapshot to {snapshot_path.name}...")
subprocess.run([vmd_path, "-dispdev", "text", "-e", str(render_tcl_path)], check=True)

#subprocess.run(["vmd", "-dispdev", "text", "-e", str(render_tcl_path)], check=True)

print("Process completed: ligand extracted and visualized.")
