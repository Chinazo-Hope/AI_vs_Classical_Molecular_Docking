
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U0D.pdb
set sel [atomselect top "resname DMS and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_29_6U0D/BRD4-BD1_BRD4-BD1_29_6U0D.pdb
quit
