
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6JI4.pdb
set sel [atomselect top "resname BOF and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_11_6JI4/BRD4-BD1_BRD4-BD1_11_6JI4.pdb
quit
