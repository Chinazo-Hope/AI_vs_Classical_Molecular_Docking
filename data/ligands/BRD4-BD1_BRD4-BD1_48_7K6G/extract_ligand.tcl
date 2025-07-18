
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7K6G.pdb
set sel [atomselect top "resname VYJ and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_48_7K6G/BRD4-BD1_BRD4-BD1_48_7K6G.pdb
quit
