
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7REM.pdb
set sel [atomselect top "resname 4OF and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_10_7REM/BRD4-BD1_BRD4-BD1_10_7REM.pdb
quit
