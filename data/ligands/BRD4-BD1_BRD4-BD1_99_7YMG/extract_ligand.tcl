
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7YMG.pdb
set sel [atomselect top "resname FMT and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_99_7YMG/BRD4-BD1_BRD4-BD1_99_7YMG.pdb
quit
