
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6PS9.pdb
set sel [atomselect top "resname Y17 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_95_6PS9/BRD4-BD1_BRD4-BD1_95_6PS9.pdb
quit
