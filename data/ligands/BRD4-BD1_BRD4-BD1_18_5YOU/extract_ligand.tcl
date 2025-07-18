
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5YOU.pdb
set sel [atomselect top "resname 8XX and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_18_5YOU/BRD4-BD1_BRD4-BD1_18_5YOU.pdb
quit
