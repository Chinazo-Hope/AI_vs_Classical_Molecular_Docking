
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6YQO.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_63_6YQO/BRD4-BD1_BRD4-BD1_63_6YQO.pdb
quit
