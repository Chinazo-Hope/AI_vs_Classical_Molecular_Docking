
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8AEV.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_28_8AEV/AChE_28_8AEV.pdb
quit
