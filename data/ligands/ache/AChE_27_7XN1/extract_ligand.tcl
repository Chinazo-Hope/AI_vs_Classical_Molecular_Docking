
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7XN1.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_27_7XN1/AChE_27_7XN1.pdb
quit
