
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/4EY8.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_60_4EY8/AChE_60_4EY8.pdb
quit
