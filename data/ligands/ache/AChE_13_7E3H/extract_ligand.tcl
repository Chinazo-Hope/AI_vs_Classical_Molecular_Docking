
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7E3H.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_13_7E3H/AChE_13_7E3H.pdb
quit
