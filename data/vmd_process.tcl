# Usage:
# vmd -dispdev text -e vmd_process.tcl -args full_input.pdb RESNAME output_base_path

set input_pdb [lindex $argv 0]
set resname [lindex $argv 1]
set output_prefix [lindex $argv 2]

# Step 1: Load original PDB
mol new $input_pdb

# Step 2: Select the ligand by residue name
set sel [atomselect top "resname $resname"]

# Step 3: Write ligand-only PDB
$sel writepdb "${output_prefix}.pdb"

# Step 4: Load ligand-only structure for rendering
mol new "${output_prefix}.pdb"
display projection orthographic
color Display Background white

# Step 5: Render PNG image
render Tachyon "${output_prefix}.png"

quit
