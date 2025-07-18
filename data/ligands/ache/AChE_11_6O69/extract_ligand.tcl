
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6O69.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_11_6O69/AChE_11_6O69.pdb
quit
