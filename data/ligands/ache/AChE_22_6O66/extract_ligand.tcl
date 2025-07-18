
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6O66.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_22_6O66/AChE_22_6O66.pdb
quit
