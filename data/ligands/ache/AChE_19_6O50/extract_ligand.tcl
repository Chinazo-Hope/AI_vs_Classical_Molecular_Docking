
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6O50.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_19_6O50/AChE_19_6O50.pdb
quit
