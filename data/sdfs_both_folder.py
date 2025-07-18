"""
organize_sdfs_by_target.py

Creates a new top-level folder structure in HopeMScP:
- HopeMScP/sdfs/ache/ : for ligands from AChE
- HopeMScP/sdfs/bd2/  : for ligands from BRD4-BD2

Moves all .sdf files from HopeMScP/data/ligands_sdf/ into the correct target subfolder
based on their filename prefix ('AChE' or 'BRD4_BD2').

Author: Chinazo Emeh
Date: July 2025
"""

from pathlib import Path
import shutil

# === Define directories === #
project_dir = Path("/Users/chinazoemeh/HopeMScP")

# Source: where your .sdf files currently are
sdf_input_dir = project_dir / "data" / "ligands_sdf"

# Destination: new top-level folder (not inside data/)
sdf_output_root = project_dir / "sdfs"
sdf_ache_dir = sdf_output_root / "ache"
sdf_bd2_dir = sdf_output_root / "bd2"

# Create destination folders if they don't exist
sdf_ache_dir.mkdir(parents=True, exist_ok=True)
sdf_bd2_dir.mkdir(parents=True, exist_ok=True)

# === Move files === #
moved_ache, moved_bd2 = 0, 0

for sdf_file in sdf_input_dir.glob("*.sdf"):
    file_name = sdf_file.name

    if file_name.startswith("AChE"):
        shutil.move(str(sdf_file), sdf_ache_dir / file_name)
        moved_ache += 1
    elif file_name.startswith("BRD4_BD2"):
        shutil.move(str(sdf_file), sdf_bd2_dir / file_name)
        moved_bd2 += 1
    else:
        print(f"⚠️ Skipped: Unknown or unlabelled file '{file_name}'")

# === Final report === #
print(f"\n✅ Moved {moved_ache} files → sdfs/ache/")
print(f"✅ Moved {moved_bd2} files → sdfs/bd2/")
