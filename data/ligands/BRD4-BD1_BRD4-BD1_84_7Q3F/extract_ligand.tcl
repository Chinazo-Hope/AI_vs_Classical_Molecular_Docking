
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7Q3F.pdb
set sel [atomselect top "resname 8M6 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_84_7Q3F/BRD4-BD1_BRD4-BD1_84_7Q3F.pdb
quit
