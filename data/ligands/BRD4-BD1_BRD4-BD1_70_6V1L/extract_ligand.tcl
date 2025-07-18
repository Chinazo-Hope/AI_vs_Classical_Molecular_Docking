
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6V1L.pdb
set sel [atomselect top "resname 5U6 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_70_6V1L/BRD4-BD1_BRD4-BD1_70_6V1L.pdb
quit
