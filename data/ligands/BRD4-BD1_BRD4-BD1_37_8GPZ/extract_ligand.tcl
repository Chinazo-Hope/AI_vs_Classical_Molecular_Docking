
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8GPZ.pdb
set sel [atomselect top "resname FMT and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_37_8GPZ/BRD4-BD1_BRD4-BD1_37_8GPZ.pdb
quit
