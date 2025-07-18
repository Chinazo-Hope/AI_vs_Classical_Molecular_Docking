"""
vmd_extract_ligands_batch_test.py

TEST SCRIPT: Automates ligand extraction and rendering from PDB protein-ligand complexes using VMD.

This version processes the first 5 ligands from the validated CSV file and outputs:
- Ligand-only .pdb file
- Rendered .png image using Licorice + AOShiny
- TCL scripts used for each step
All outputs are labeled with 'TEST' and stored in individual folders.

Inputs:
- ligand_mapping_validated.csv with columns: UniqueID, PDB_ID, Ligand(s)

Author: Chinazo Emeh
Date: July 2025
"""

import csv
import requests
import subprocess
from pathlib import Path
import platform

# === Define base project directories === #
project_dir = Path("/Users/chinazoemeh/HopeMScP")
csv_path = project_dir / "data" / "ligand_mapping_validated.csv"
pdb_download_dir = project_dir / "data" / "pdb_files"
ligands_output_base = project_dir / "data" / "ligands"

# Ensure folders exist
pdb_download_dir.mkdir(parents=True, exist_ok=True)
ligands_output_base.mkdir(parents=True, exist_ok=True)

# === Define VMD path depending on OS === #
if platform.system() == "Darwin":
    vmd_path = "/Applications/VMD 1.9.4a57-arm64-Rev12.app/Contents/vmd/vmd_MACOSXARM64"
else:
    vmd_path = "vmd"

# === Process first 5 ligands from CSV === #
with open(csv_path, "r", newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for i, row in enumerate(reader):
        if i >= 5:
            break

        # Extract details for each ligand
        unique_id = f"BRD4-BD1_TEST_{row['UniqueID']}_{row['PDB_ID']}"
        pdb_id = row["PDB_ID"]
        ligand_resname = row["Ligand(s)"]  # Updated field name

        print(f"\nProcessing {pdb_id} (Ligand: {ligand_resname})")

        # === Step 1: Download the PDB file if not present === #
        pdb_filename = f"{pdb_id}.pdb"
        pdb_local_path = pdb_download_dir / pdb_filename

        if not pdb_local_path.exists():
            pdb_url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
            print(f"Downloading {pdb_url}")
            response = requests.get(pdb_url)
            response.raise_for_status()
            pdb_local_path.write_text(response.text)
        else:
            print(f"Using cached PDB: {pdb_filename}")

        # === Step 2: Create a unique output folder for this ligand === #
        output_folder = ligands_output_base / unique_id
        output_folder.mkdir(parents=True, exist_ok=True)

        ligand_only_path = output_folder / f"{unique_id}.pdb"
        snapshot_path = output_folder / f"{unique_id}.png"

        # === Step 3: Write the ligand extraction TCL script === #
        extract_tcl_path = output_folder / "extract_ligand.tcl"
        extract_tcl_path.write_text(f"""
mol new {pdb_local_path}
set sel [atomselect top "resname {ligand_resname} and not water"]
$sel writepdb {ligand_only_path}
quit
""")

        # === Step 4: Write the rendering TCL script === #
        render_tcl_path = output_folder / "render.tcl"
        render_tcl_path.write_text(f"""
mol new {ligand_only_path}
display projection orthographic
color Display Background white
mol delrep 0 top
mol representation Licorice 0.3 12 12
mol color Name
mol material AOShiny
mol selection all
mol addrep top
render wait on
render Tachyon {snapshot_path}
quit
""")

        # === Step 5: Run VMD to extract the ligand === #
        print(f"Extracting ligand from {pdb_id}...")
        subprocess.run([vmd_path, "-dispdev", "text", "-e", str(extract_tcl_path)], check=True)

        # === Step 6: Run VMD to render the ligand image === #
        print(f"Rendering image to {snapshot_path.name}...")
        subprocess.run([vmd_path, "-dispdev", "text", "-e", str(render_tcl_path)], check=True)

        print(f"Completed: {unique_id}")
