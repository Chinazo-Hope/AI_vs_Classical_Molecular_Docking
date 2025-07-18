
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6WV1.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_51_6WV1/AChE_51_6WV1.pdb
quit
