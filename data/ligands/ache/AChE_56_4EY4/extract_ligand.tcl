
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/4EY4.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_56_4EY4/AChE_56_4EY4.pdb
quit
