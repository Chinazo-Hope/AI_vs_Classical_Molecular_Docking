
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8DT7.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_32_8DT7/AChE_32_8DT7.pdb
quit
