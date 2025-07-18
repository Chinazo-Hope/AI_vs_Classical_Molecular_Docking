
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6F25.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_67_6F25/AChE_67_6F25.pdb
quit
