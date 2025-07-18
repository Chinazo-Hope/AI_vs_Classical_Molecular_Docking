
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/4EY6.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_58_4EY6/AChE_58_4EY6.pdb
quit
