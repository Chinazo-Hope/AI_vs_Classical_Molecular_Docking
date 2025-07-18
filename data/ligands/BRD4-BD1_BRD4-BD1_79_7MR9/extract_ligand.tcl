
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7MR9.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_79_7MR9/BRD4-BD1_BRD4-BD1_79_7MR9.pdb
quit
