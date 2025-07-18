
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8AEN.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_55_8AEN/AChE_55_8AEN.pdb
quit
