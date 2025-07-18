
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7K6H.pdb
set sel [atomselect top "resname 4WG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_66_7K6H/BRD4-BD1_BRD4-BD1_66_7K6H.pdb
quit
