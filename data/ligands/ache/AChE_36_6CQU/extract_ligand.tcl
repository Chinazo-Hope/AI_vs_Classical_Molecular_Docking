
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6CQU.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_36_6CQU/AChE_36_6CQU.pdb
quit
