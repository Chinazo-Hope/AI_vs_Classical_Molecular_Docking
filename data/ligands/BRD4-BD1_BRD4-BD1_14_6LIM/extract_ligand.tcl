
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6LIM.pdb
set sel [atomselect top "resname EE9 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_14_6LIM/BRD4-BD1_BRD4-BD1_14_6LIM.pdb
quit
