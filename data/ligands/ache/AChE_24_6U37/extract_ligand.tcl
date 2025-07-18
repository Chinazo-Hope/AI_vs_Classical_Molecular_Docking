
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U37.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_24_6U37/AChE_24_6U37.pdb
quit
