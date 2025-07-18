
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8B96.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_TEST_BRD4-BD1_2_8B96/BRD4-BD1_TEST_BRD4-BD1_2_8B96.pdb
quit
