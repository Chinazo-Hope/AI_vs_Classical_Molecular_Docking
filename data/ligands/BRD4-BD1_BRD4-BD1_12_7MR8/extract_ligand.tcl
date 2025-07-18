
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7MR8.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_12_7MR8/BRD4-BD1_BRD4-BD1_12_7MR8.pdb
quit
