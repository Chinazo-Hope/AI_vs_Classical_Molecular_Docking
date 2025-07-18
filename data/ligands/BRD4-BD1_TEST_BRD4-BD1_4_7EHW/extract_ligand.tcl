
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7EHW.pdb
set sel [atomselect top "resname J4O and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_TEST_BRD4-BD1_4_7EHW/BRD4-BD1_TEST_BRD4-BD1_4_7EHW.pdb
quit
