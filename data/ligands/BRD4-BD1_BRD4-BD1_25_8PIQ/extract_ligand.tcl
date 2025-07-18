
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8PIQ.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_25_8PIQ/BRD4-BD1_BRD4-BD1_25_8PIQ.pdb
quit
