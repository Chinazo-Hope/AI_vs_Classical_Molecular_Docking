
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U6K.pdb
set sel [atomselect top "resname ALY and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_102_6U6K/BRD4-BD1_BRD4-BD1_102_6U6K.pdb
quit
