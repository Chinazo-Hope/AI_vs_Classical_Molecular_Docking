"""
Final script: Extracts and renders a ligand from a protein-ligand complex using VMD.

- Extracts by resname (e.g., 7QZ)
- Renders in high-quality Licorice style (AOShiny)
- Saves PDB and PNG in structured folders

Author: Chinazo Emeh
Date: July 2025
"""

import subprocess
from pathlib import Path
import platform

# === CONFIGURATION === #
unique_id = "BRD4-BD1_1_7RUI"         # Unique folder and output naming
pdb_filename = "7RUI.pdb"             # Full complex PDB file
ligand_resname = "7QZ"                # Ligand resname from PDB

# === PATH SETUP === #
project_dir = Path("/Users/chinazoemeh/HopeMScP")  # Update if needed
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

# === TCL SCRIPT TO RENDER LIGAND IN LICORICE + AOShiny === #
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
render Tachyon {snapshot_path}
quit
"""

render_tcl_path = output_folder / "render.tcl"
render_tcl_path.write_text(render_script)

# === VMD EXECUTABLE === #
if platform.system() == "Darwin":
    # Mac-specific path
    vmd_path = "/Applications/VMD 1.9.4a57-arm64-Rev12.app/Contents/vmd/vmd_MACOSXARM64"
else:
    vmd_path = "vmd"  # For ThinLinc/HPC

# === RUN VMD TO EXTRACT LIGAND === #
print(f"Extracting ligand from {pdb_filename}...")
subprocess.run([vmd_path, "-dispdev", "text", "-e", str(extract_tcl_path)], check=True)

# === RUN VMD TO RENDER PNG === #
print(f"Rendering PNG snapshot to {snapshot_path.name}...")
subprocess.run([vmd_path, "-dispdev", "text", "-e", str(render_tcl_path)], check=True)

print("✅ Ligand extracted and rendered successfully.")
