
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7RB6.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_26_7RB6/AChE_26_7RB6.pdb
quit
