
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7RUI.pdb
set sel [atomselect top "resname 7QZ and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_1_7RUI_test/BRD4-BD1_1_7RUI_test.pdb
quit
