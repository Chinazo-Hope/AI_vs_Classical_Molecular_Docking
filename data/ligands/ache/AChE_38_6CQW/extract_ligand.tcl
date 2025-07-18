
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6CQW.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_38_6CQW/AChE_38_6CQW.pdb
quit
