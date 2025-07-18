
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6NTO.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_47_6NTO/AChE_47_6NTO.pdb
quit
