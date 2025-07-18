
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6FNX.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_40_6FNX/BRD4-BD1_BRD4-BD1_40_6FNX.pdb
quit
