
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U72.pdb
set sel [atomselect top "resname ALY and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_107_6U72/BRD4-BD1_BRD4-BD1_107_6U72.pdb
quit
