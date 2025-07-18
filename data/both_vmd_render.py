"""
vmd_extract_ligands_both.py

Automates ligand extraction and 3D rendering for both AChE and BRD4-BD2 targets.

Inputs:
- ligand_mapping_ache_cleaned_only.csv
- ligand_mapping_bd2_cleaned_only.csv

Each ligand is saved in a dedicated folder with:
- Original PDB file from RCSB
- Ligand-only .pdb
- 3D image (.png) using Licorice + AOShiny
- Extract and render TCL scripts

Output Folders:
- data/ligands/ache/UniqueID_PDBID/
- data/ligands/bd2/UniqueID_PDBID/

Author: Chinazo Emeh
Date: July 2025
"""

import csv
import requests
import subprocess
from pathlib import Path
import platform

# === Paths === #
project_dir = Path("/Users/chinazoemeh/HopeMScP")
pdb_download_dir = project_dir / "data" / "pdb_files"
ligands_output_base = project_dir / "data" / "ligands"
ache_csv = project_dir / "data" / "ligand_mapping_ache_cleaned_only.csv"
bd2_csv = project_dir / "data" / "ligand_mapping_bd2_cleaned_only.csv"

# Create output folders
for sub in ["ache", "bd2"]:
    (ligands_output_base / sub).mkdir(parents=True, exist_ok=True)
pdb_download_dir.mkdir(parents=True, exist_ok=True)

# OS-specific VMD path
vmd_path = "/Applications/VMD 1.9.4a57-arm64-Rev12.app/Contents/vmd/vmd_MACOSXARM64" if platform.system() == "Darwin" else "vmd"

# === Function to process a single CSV === #
def process_csv(csv_file, target_subdir):
    with open(csv_file, "r", newline='') as file:
        reader = csv.DictReader(file)
        count = 0

        for row in reader:
            unique_id = row["UniqueID"]
            pdb_id = row["PDB_ID"].strip().upper()
            ligand = row["Ligand(s)"].strip()

            if not pdb_id or not ligand or ligand.lower() == "none":
                print(f"⚠️ Skipping {unique_id}: Missing ligand.")
                continue

            output_folder = ligands_output_base / target_subdir / f"{unique_id}_{pdb_id}"
            output_folder.mkdir(parents=True, exist_ok=True)

            # === Download original PDB === #
            pdb_url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
            pdb_local_path = pdb_download_dir / f"{pdb_id}.pdb"
            if not pdb_local_path.exists():
                try:
                    print(f"⬇️ Downloading {pdb_id}...")
                    response = requests.get(pdb_url)
                    response.raise_for_status()
                    pdb_local_path.write_text(response.text)
                except Exception as e:
                    print(f"❌ Failed to download {pdb_id}: {e}")
                    continue
            else:
                print(f"✅ Using cached PDB for {pdb_id}")

            ligand_pdb = output_folder / f"{unique_id}_{pdb_id}.pdb"
            image_path = output_folder / f"{unique_id}_{pdb_id}.png"

            # === Extract TCL === #
            extract_script = output_folder / "extract_ligand.tcl"
            extract_script.write_text(f"""
mol new {pdb_local_path}
set sel [atomselect top "resname {ligand} and not water"]
$sel writepdb {ligand_pdb}
quit
""")

            # === Render TCL === #
            render_script = output_folder / "render.tcl"
            render_script.write_text(f"""
mol new {ligand_pdb}
display projection orthographic
color Display Background white
mol delrep 0 top
mol representation Licorice 0.3 12 12
mol color Name
mol material AOShiny
mol selection all
mol addrep top
render wait on
render Tachyon {image_path}
quit
""")

            try:
                print(f"🔬 Extracting ligand: {unique_id}")
                subprocess.run([vmd_path, "-dispdev", "text", "-e", str(extract_script)], check=True)

                print(f"🖼 Rendering: {image_path.name}")
                subprocess.run([vmd_path, "-dispdev", "text", "-e", str(render_script)], check=True)

                count += 1
            except subprocess.CalledProcessError as e:
                print(f"❌ VMD failed for {unique_id}: {e}")

        print(f"\n✅ Finished {count} entries from {csv_file.name} → {target_subdir}/\n")

# === Run for both targets === #
process_csv(ache_csv, "ache")
process_csv(bd2_csv, "bd2")

print("🎉 Ligand extraction + rendering complete for AChE and BRD4-BD2.")
