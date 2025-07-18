
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6JI3.pdb
set sel [atomselect top "resname BW6 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_23_6JI3/BRD4-BD1_BRD4-BD1_23_6JI3.pdb
quit
