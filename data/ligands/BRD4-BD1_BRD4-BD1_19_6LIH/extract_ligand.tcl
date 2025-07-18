
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6LIH.pdb
set sel [atomselect top "resname EDF and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_19_6LIH/BRD4-BD1_BRD4-BD1_19_6LIH.pdb
quit
