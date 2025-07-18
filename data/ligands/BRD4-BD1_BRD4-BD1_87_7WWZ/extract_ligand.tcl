
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7WWZ.pdb
set sel [atomselect top "resname 7OW and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_87_7WWZ/BRD4-BD1_BRD4-BD1_87_7WWZ.pdb
quit
