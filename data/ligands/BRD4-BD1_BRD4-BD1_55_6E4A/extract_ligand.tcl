
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6E4A.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_55_6E4A/BRD4-BD1_BRD4-BD1_55_6E4A.pdb
quit
