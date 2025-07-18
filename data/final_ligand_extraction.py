"""
extract_ligands_batch_vmd.py

Description:
------------
This script automates the extraction and rendering of ligands from 3D protein-ligand crystal structures using VMD (Visual Molecular Dynamics).
It processes all entries in the validated ligand mapping CSV file, downloads the corresponding PDB structures (if not already cached),
isolates the ligand using its residue name, and renders a high-quality image of the ligand structure using the "Bonds" representation.

Each ligand's output is saved into a clean, dedicated folder:
- Extracted ligand as a .pdb file
- Rendered image as a .png file (AOShiny material, orthographic projection)
- TCL scripts used for both extraction and rendering

File and folder naming is standardized using this format:
  BRD4-BD1_<UniqueID>_<PDB_ID>

Inputs:
-------
- CSV file: `ligand_mapping_validated.csv` located at /data/
  with columns: UniqueID, PDB_ID, Ligand(s)
- VMD installed on macOS or Linux

Outputs:
--------
- Extracted .pdb file of the ligand
- Rendered .png image
- Two .tcl scripts used by VMD for each ligand

Author: Chinazo Emeh
Date: 14th July 2025
"""

import csv
import requests
import subprocess
from pathlib import Path
import platform

# === Step 1: Define key directories === #
project_dir = Path("/Users/chinazoemeh/HopeMScP")

# Path to CSV containing 96 ligand entries
csv_path = project_dir / "data" / "ligand_mapping_validated.csv"

# Local cache for downloaded PDB structures
pdb_download_dir = project_dir / "data/pdb_files"

# Output location for ligand-only files and images
ligands_output_base = project_dir / "data/ligands"

# Ensure folders exist
pdb_download_dir.mkdir(parents=True, exist_ok=True)
ligands_output_base.mkdir(parents=True, exist_ok=True)

# === Step 2: Define VMD executable path depending on operating system === #
if platform.system() == "Darwin":
    # macOS-specific VMD path (adjust if your install differs)
    vmd_path = "/Applications/VMD 1.9.4a57-arm64-Rev12.app/Contents/vmd/vmd_MACOSXARM64"
else:
    # On ThinLinc or Linux, we assume VMD is in PATH
    vmd_path = "vmd"

# === Step 3: Read CSV and loop through all ligands === #
with open(csv_path, "r", newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # Extract identifiers
        unique_id = f"BRD4-BD1_{row['UniqueID']}_{row['PDB_ID']}"
        pdb_id = row["PDB_ID"]
        ligand_resname = row["Ligand(s)"]

        print(f"\nProcessing {pdb_id} (Ligand: {ligand_resname})")

        # === Step 4: Download PDB file if it hasn't been cached === #
        pdb_filename = f"{pdb_id}.pdb"
        pdb_local_path = pdb_download_dir / pdb_filename

        if not pdb_local_path.exists():
            pdb_url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
            print(f"Downloading PDB file from: {pdb_url}")
            response = requests.get(pdb_url)
            response.raise_for_status()
            pdb_local_path.write_text(response.text)
        else:
            print(f"Using cached PDB file: {pdb_filename}")

        # === Step 5: Set up output directory and filenames === #
        output_folder = ligands_output_base / unique_id
        output_folder.mkdir(parents=True, exist_ok=True)

        ligand_only_path = output_folder / f"{unique_id}.pdb"
        snapshot_path = output_folder / f"{unique_id}.png"

        # === Step 6: Generate TCL script for ligand extraction === #
        extract_tcl = f"""
mol new {pdb_local_path}
set sel [atomselect top "resname {ligand_resname} and not water"]
$sel writepdb {ligand_only_path}
quit
"""
        extract_tcl_path = output_folder / "extract_ligand.tcl"
        extract_tcl_path.write_text(extract_tcl)

        # === Step 7: Generate TCL script for rendering ligand image === #
        render_tcl = f"""
mol new {ligand_only_path}
display projection orthographic
color Display Background white
mol delrep 0 top
mol representation Bonds 0.3
mol color Name
mol material AOShiny
mol selection all
mol addrep top
render Tachyon {snapshot_path}
quit
"""
        render_tcl_path = output_folder / "render.tcl"
        render_tcl_path.write_text(render_tcl)

        # === Step 8: Run VMD to extract ligand === #
        print(f"Extracting ligand using VMD...")
        subprocess.run([vmd_path, "-dispdev", "text", "-e", str(extract_tcl_path)], check=True)

        # === Step 9: Run VMD to render the ligand image === #
        print(f"Rendering PNG image to: {snapshot_path.name}...")
        subprocess.run([vmd_path, "-dispdev", "text", "-e", str(render_tcl_path)], check=True)

        print(f" Completed: {unique_id}")
