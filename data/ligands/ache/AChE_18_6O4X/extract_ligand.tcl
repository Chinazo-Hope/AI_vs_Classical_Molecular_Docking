
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6O4X.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_18_6O4X/AChE_18_6O4X.pdb
quit
