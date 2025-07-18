
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6FO5.pdb
set sel [atomselect top "resname DZH and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_39_6FO5/BRD4-BD1_BRD4-BD1_39_6FO5.pdb
quit
