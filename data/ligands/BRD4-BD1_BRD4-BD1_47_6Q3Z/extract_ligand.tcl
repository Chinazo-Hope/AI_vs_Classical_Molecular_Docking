
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6Q3Z.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_47_6Q3Z/BRD4-BD1_BRD4-BD1_47_6Q3Z.pdb
quit
