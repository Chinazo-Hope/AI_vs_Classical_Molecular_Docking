"""
convert_pdbs_to_sdfs_by_target.py

Converts ligand-only `.pdb` files from AChE and BRD4-BD2 targets into `.sdf` format using Open Babel.
Each converted `.sdf` is saved under a dedicated folder structure:

  HopeMScP/
  └── sdfs/
      ├── ache/
      └── bd2/

Author: Chinazo Emeh
Date: July 2025
"""

import subprocess
from pathlib import Path

# === Base directories === #
project_dir = Path("/Users/chinazoemeh/HopeMScP")
ligands_dir = project_dir / "data" / "ligands"
sdfs_root = project_dir / "sdfs"

# === Create target folders if they don't exist === #
ache_sdf_dir = sdfs_root / "ache"
bd2_sdf_dir = sdfs_root / "bd2"
ache_sdf_dir.mkdir(parents=True, exist_ok=True)
bd2_sdf_dir.mkdir(parents=True, exist_ok=True)

# === Conversion loop === #
converted_count = 0
for target in ["ache", "bd2"]:
    source_folder = ligands_dir / target
    output_folder = ache_sdf_dir if target == "ache" else bd2_sdf_dir

    for pdb_file in source_folder.rglob("*.pdb"):
        base_name = pdb_file.stem
        sdf_path = output_folder / f"{base_name}.sdf"

        try:
            subprocess.run(["obabel", str(pdb_file), "-O", str(sdf_path)], check=True)
            print(f"✅ Converted {base_name}.pdb → {sdf_path.name}")
            converted_count += 1
        except subprocess.CalledProcessError:
            print(f"❌ Failed to convert {base_name}.pdb")

print(f"\n🎉 Finished converting {converted_count} PDBs to SDFs.")
