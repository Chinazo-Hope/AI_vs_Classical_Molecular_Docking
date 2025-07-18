
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6JI5.pdb
set sel [atomselect top "resname BQ0 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_16_6JI5/BRD4-BD1_BRD4-BD1_16_6JI5.pdb
quit
