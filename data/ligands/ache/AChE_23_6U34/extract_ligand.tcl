
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U34.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_23_6U34/AChE_23_6U34.pdb
quit
