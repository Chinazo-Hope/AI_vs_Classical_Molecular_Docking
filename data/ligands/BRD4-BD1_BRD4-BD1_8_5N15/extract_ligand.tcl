
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5N15.pdb
set sel [atomselect top "resname IOD and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_8_5N15/BRD4-BD1_BRD4-BD1_8_5N15.pdb
quit
