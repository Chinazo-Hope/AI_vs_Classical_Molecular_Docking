
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6NEA.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_41_6NEA/AChE_41_6NEA.pdb
quit
