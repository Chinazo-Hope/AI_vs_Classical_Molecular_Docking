
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/1F8U.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_71_1F8U/AChE_71_1F8U.pdb
quit
