
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8B98.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_3_8B98/BRD4-BD1_BRD4-BD1_3_8B98.pdb
quit
