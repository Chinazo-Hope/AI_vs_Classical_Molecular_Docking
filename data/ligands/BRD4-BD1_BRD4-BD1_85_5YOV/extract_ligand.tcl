
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5YOV.pdb
set sel [atomselect top "resname 8XR and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_85_5YOV/BRD4-BD1_BRD4-BD1_85_5YOV.pdb
quit
