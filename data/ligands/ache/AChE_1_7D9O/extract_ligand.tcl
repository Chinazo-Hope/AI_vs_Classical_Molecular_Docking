
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7D9O.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_1_7D9O/AChE_1_7D9O.pdb
quit
