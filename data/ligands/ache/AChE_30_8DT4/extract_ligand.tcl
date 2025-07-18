
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8DT4.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_30_8DT4/AChE_30_8DT4.pdb
quit
