
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7JKX.pdb
set sel [atomselect top "resname Y36 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_13_7JKX/BRD4-BD1_BRD4-BD1_13_7JKX.pdb
quit
