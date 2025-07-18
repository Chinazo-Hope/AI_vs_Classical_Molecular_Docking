
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8WQO.pdb
set sel [atomselect top "resname X3L and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_83_8WQO/BRD4-BD1_BRD4-BD1_83_8WQO.pdb
quit
