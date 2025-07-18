
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/4M0F.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_61_4M0F/AChE_61_4M0F.pdb
quit
