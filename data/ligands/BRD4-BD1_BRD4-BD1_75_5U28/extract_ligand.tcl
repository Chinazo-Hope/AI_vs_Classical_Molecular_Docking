
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5U28.pdb
set sel [atomselect top "resname 82V and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_75_5U28/BRD4-BD1_BRD4-BD1_75_5U28.pdb
quit
