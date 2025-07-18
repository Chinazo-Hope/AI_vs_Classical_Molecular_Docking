
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6O4W.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_17_6O4W/AChE_17_6O4W.pdb
quit
