
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6XUZ.pdb
set sel [atomselect top "resname O1W and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_78_6XUZ/BRD4-BD1_BRD4-BD1_78_6XUZ.pdb
quit
