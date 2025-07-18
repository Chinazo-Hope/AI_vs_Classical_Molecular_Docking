
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/1VZJ.pdb
set sel [atomselect top "resname MSE and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_74_1VZJ/AChE_74_1VZJ.pdb
quit
