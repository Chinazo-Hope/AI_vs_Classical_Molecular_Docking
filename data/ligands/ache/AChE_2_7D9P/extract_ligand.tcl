
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7D9P.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_2_7D9P/AChE_2_7D9P.pdb
quit
