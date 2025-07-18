
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6WUZ.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_50_6WUZ/AChE_50_6WUZ.pdb
quit
