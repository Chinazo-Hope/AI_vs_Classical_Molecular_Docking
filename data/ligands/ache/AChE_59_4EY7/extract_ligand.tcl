
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/4EY7.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_59_4EY7/AChE_59_4EY7.pdb
quit
