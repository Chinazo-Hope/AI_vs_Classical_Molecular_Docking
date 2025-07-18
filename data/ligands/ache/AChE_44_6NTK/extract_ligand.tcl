
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6NTK.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_44_6NTK/AChE_44_6NTK.pdb
quit
