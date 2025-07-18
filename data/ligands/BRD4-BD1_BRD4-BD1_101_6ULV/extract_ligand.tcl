
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6ULV.pdb
set sel [atomselect top "resname IOD and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_101_6ULV/BRD4-BD1_BRD4-BD1_101_6ULV.pdb
quit
