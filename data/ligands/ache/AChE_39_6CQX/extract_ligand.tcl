
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6CQX.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_39_6CQX/AChE_39_6CQX.pdb
quit
