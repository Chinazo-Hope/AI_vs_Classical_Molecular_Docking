
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6WVC.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_52_6WVC/AChE_52_6WVC.pdb
quit
