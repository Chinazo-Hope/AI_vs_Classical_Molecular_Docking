
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/4M0E.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_33_4M0E/AChE_33_4M0E.pdb
quit
