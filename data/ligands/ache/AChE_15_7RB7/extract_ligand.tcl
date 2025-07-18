
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7RB7.pdb
set sel [atomselect top "resname NWA and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_15_7RB7/AChE_15_7RB7.pdb
quit
