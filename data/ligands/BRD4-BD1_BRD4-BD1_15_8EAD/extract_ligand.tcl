
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8EAD.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_15_8EAD/BRD4-BD1_BRD4-BD1_15_8EAD.pdb
quit
