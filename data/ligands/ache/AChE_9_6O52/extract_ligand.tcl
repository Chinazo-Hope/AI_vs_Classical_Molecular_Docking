
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6O52.pdb
set sel [atomselect top "resname EBW and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_9_6O52/AChE_9_6O52.pdb
quit
