
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6CQZ.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_40_6CQZ/AChE_40_6CQZ.pdb
quit
