
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6ULS.pdb
set sel [atomselect top "resname ALY and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_109_6ULS/BRD4-BD1_BRD4-BD1_109_6ULS.pdb
quit
