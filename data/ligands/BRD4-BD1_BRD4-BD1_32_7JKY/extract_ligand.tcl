
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7JKY.pdb
set sel [atomselect top "resname YF6 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_32_7JKY/BRD4-BD1_BRD4-BD1_32_7JKY.pdb
quit
