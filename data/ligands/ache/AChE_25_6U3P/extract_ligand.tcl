
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U3P.pdb
set sel [atomselect top "resname PQY and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_25_6U3P/AChE_25_6U3P.pdb
quit
