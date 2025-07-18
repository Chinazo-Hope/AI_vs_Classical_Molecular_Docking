
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6CQY.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_66_6CQY/AChE_66_6CQY.pdb
quit
