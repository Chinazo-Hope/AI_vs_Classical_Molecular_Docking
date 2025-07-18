
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6WVO.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_68_6WVO/AChE_68_6WVO.pdb
quit
