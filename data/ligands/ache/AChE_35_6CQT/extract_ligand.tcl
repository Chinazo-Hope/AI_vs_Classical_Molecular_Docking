
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6CQT.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_35_6CQT/AChE_35_6CQT.pdb
quit
