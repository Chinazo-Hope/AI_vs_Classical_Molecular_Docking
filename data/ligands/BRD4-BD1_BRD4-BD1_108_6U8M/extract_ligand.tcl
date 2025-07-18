
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U8M.pdb
set sel [atomselect top "resname ALY and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_108_6U8M/BRD4-BD1_BRD4-BD1_108_6U8M.pdb
quit
