
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6G0D.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_61_6G0D/BRD4-BD1_BRD4-BD1_61_6G0D.pdb
quit
