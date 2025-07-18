
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/9FXP.pdb
set sel [atomselect top "resname 5WX and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_97_9FXP/BRD4-BD1_BRD4-BD1_97_9FXP.pdb
quit
