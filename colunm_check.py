import pandas as pd

# Load the Excel file
df = pd.read_excel("dual_ligand_database.xlsx")

# Print exact column names to diagnose the issue
print("Column names found in Excel:")
for col in df.columns:
    print(f"'{col}'")

