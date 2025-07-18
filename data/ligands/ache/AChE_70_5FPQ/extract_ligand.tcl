
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5FPQ.pdb
set sel [atomselect top "resname SGB and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_70_5FPQ/AChE_70_5FPQ.pdb
quit
