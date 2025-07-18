
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6WUV.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_48_6WUV/AChE_48_6WUV.pdb
quit
