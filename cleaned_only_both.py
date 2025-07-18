"""
Script Name: cleaned_only_both.py
Author: Chinazo Emeh
Date: 2025-07-17

Description:
------------
This script reads ligand mapping CSV files for AChE and BRD4-BD2,
drops invalid ligand rows (NaN, 'None', 'N/A', or empty),
and saves cleaned versions with a preview summary.
"""

import pandas as pd
from pathlib import Path

# --- File paths ---
data_dir = Path("data")
ache_path = data_dir / "ligand_mapping_ache.csv"
bd2_path = data_dir / "ligand_mapping_bd2.csv"
ache_output = data_dir / "ligand_mapping_ache_cleaned_only.csv"
bd2_output = data_dir / "ligand_mapping_bd2_cleaned_only.csv"

# --- Load data with error handling ---
try:
    df_ache = pd.read_csv(ache_path)
    print(f"✅ Loaded AChE CSV with {len(df_ache)} rows.")
except Exception as e:
    print(f"❌ Failed to load AChE CSV: {e}")
    df_ache = pd.DataFrame()

try:
    df_bd2 = pd.read_csv(bd2_path)
    print(f"✅ Loaded BD2 CSV with {len(df_bd2)} rows.")
except Exception as e:
    print(f"❌ Failed to load BD2 CSV: {e}")
    df_bd2 = pd.DataFrame()

# --- Drop invalid rows where Ligand(s) is None, N/A, NaN or empty ---
invalid_entries = {"None", "N/A", ""}
df_ache_clean = df_ache[~df_ache["Ligand(s)"].isin(invalid_entries)]
df_ache_clean = df_ache_clean.dropna(subset=["Ligand(s)"])
print(f"🧹 Cleaned AChE: {len(df_ache_clean)} valid entries remaining.")

df_bd2_clean = df_bd2[~df_bd2["Ligand(s)"].isin(invalid_entries)]
df_bd2_clean = df_bd2_clean.dropna(subset=["Ligand(s)"])
print(f"🧹 Cleaned BD2: {len(df_bd2_clean)} valid entries remaining.")

# --- Save cleaned files ---
df_ache_clean.to_csv(ache_output, index=False)
print(f"✅ Saved cleaned AChE CSV to: {ache_output.resolve()}")

df_bd2_clean.to_csv(bd2_output, index=False)
print(f"✅ Saved cleaned BD2 CSV to: {bd2_output.resolve()}")

# --- Show preview ---
print("\n🔍 Preview of cleaned AChE (first 5 rows):")
print(df_ache_clean.head(5), "\n")

print("🔍 Preview of cleaned BD2 (first 5 rows):")
print(df_bd2_clean.head(5))
