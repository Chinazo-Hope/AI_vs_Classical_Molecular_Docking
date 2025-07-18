
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6WUY.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_49_6WUY/AChE_49_6WUY.pdb
quit
