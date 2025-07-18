
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7EHY.pdb
set sel [atomselect top "resname YD8 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_TEST_BRD4-BD1_5_7EHY/BRD4-BD1_TEST_BRD4-BD1_5_7EHY.pdb
quit
