
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7X6T.pdb
set sel [atomselect top "resname 97F and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_26_7X6T/BRD4-BD1_BRD4-BD1_26_7X6T.pdb
quit
