
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6YQP.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_67_6YQP/BRD4-BD1_BRD4-BD1_67_6YQP.pdb
quit
