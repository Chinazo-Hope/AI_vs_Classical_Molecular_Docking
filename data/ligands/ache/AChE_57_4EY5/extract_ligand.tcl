
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/4EY5.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_57_4EY5/AChE_57_4EY5.pdb
quit
