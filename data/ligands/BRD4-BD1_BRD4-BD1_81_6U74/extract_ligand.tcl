
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U74.pdb
set sel [atomselect top "resname ALY and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_81_6U74/BRD4-BD1_BRD4-BD1_81_6U74.pdb
quit
