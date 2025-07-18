
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7FH2.pdb
set sel [atomselect top "resname 4JI and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_72_7FH2/BRD4-BD1_BRD4-BD1_72_7FH2.pdb
quit
