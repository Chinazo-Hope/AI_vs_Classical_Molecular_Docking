"""
Script to extract and render a ligand from a protein-ligand complex using VMD.
- Saves outputs using the ID: BRD4-BD1_1_7RUI_test
- Uses high-quality Licorice + AOShiny rendering
- Avoids overwriting other runs

Author: Chinazo Emeh
Date: July 2025
"""

import subprocess
from pathlib import Path
import platform

# === CONFIGURATION === #
unique_id = "BRD4-BD1_1_7RUI_test"     # NEW unique output name for this test
pdb_filename = "7RUI.pdb"              # Full complex PDB file
ligand_resname = "7QZ"                 # Ligand resname from PDB

# === PATH SETUP === #
project_dir = Path("/Users/chinazoemeh/HopeMScP")  # Adjust if needed
input_pdb_dir = project_dir / "data/pdb_files"
output_folder = project_dir / "data/ligands" / unique_id
output_folder.mkdir(parents=True, exist_ok=True)

pdb_path = input_pdb_dir / pdb_filename
ligand_only_path = output_folder / f"{unique_id}.pdb"
snapshot_path = output_folder / f"{unique_id}.png"

# === TCL SCRIPT TO EXTRACT LIGAND === #
vmd_extract_script = f"""
mol new {pdb_path}
set sel [atomselect top "resname {ligand_resname} and not water"]
$sel writepdb {ligand_only_path}
quit
"""
extract_tcl_path = output_folder / "extract_ligand.tcl"
extract_tcl_path.write_text(vmd_extract_script)

# === TCL SCRIPT TO RENDER IN LICORICE === #
render_script = f"""
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
"""
render_tcl_path = output_folder / "render.tcl"
render_tcl_path.write_text(render_script)

# === VMD EXECUTABLE PATH === #
if platform.system() == "Darwin":
    # macOS path (adjust if you installed VMD differently)
    vmd_path = "/Applications/VMD 1.9.4a57-arm64-Rev12.app/Contents/vmd/vmd_MACOSXARM64"
else:
    vmd_path = "vmd"  # Use module on ThinLinc or Linux

# === RUN VMD TO EXTRACT LIGAND === #
print(f"Extracting ligand from {pdb_filename}...")
subprocess.run([vmd_path, "-dispdev", "text", "-e", str(extract_tcl_path)], check=True)

# === RUN VMD TO RENDER IMAGE === #
print(f"Rendering PNG snapshot to {snapshot_path.name}...")
subprocess.run([vmd_path, "-dispdev", "text", "-e", str(render_tcl_path)], check=True)

print("✅ Ligand extracted and rendered successfully.")
