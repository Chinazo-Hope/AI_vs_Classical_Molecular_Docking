
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/2X8B.pdb
set sel [atomselect top "resname UNX and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_75_2X8B/AChE_75_2X8B.pdb
quit
