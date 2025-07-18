
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7YQ9.pdb
set sel [atomselect top "resname JLX and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_100_7YQ9/BRD4-BD1_BRD4-BD1_100_7YQ9.pdb
quit
