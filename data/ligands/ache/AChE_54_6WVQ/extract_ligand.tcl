
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6WVQ.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_54_6WVQ/AChE_54_6WVQ.pdb
quit
