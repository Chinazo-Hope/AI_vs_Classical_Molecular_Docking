"""
organize_ligand_folders.py

Organizes ligand output folders into AChE and BD2 subdirectories
based on UniqueID prefix. This keeps your workspace structured.

Author: Chinazo Emeh
Date: July 2025
"""

import os
from pathlib import Path
import shutil

# === Define base ligand folder === #
ligands_base = Path("/Users/chinazoemeh/HopeMScP/data/ligands")

# === Define destination folders === #
ache_dir = ligands_base / "ache"
bd2_dir = ligands_base / "bd2"
ache_dir.mkdir(parents=True, exist_ok=True)
bd2_dir.mkdir(parents=True, exist_ok=True)

# === Move folders === #
for folder in ligands_base.iterdir():
    if folder.is_dir():
        if folder.name.startswith("AChE_"):
            shutil.move(str(folder), str(ache_dir / folder.name))
            print(f"📦 Moved {folder.name} → ache/")
        elif folder.name.startswith("BRD4_BD2_"):
            shutil.move(str(folder), str(bd2_dir / folder.name))
            print(f"📦 Moved {folder.name} → bd2/")
        else:
            print(f"⚠️ Skipped {folder.name} (unknown prefix)")

print("\n✅ Organization complete.")
