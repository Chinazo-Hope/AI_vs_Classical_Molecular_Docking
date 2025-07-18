
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8DT5.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_31_8DT5/AChE_31_8DT5.pdb
quit
