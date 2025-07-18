
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6V1U.pdb
set sel [atomselect top "resname QMG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_77_6V1U/BRD4-BD1_BRD4-BD1_77_6V1U.pdb
quit
