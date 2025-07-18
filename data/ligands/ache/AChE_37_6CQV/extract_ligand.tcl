
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6CQV.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_37_6CQV/AChE_37_6CQV.pdb
quit
