
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7RB5.pdb
set sel [atomselect top "resname NWA and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_14_7RB5/AChE_14_7RB5.pdb
quit
