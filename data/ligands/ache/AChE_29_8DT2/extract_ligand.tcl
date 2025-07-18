
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8DT2.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_29_8DT2/AChE_29_8DT2.pdb
quit
