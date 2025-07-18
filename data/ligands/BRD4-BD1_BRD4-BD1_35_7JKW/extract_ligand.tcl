
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7JKW.pdb
set sel [atomselect top "resname VCV and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_35_7JKW/BRD4-BD1_BRD4-BD1_35_7JKW.pdb
quit
