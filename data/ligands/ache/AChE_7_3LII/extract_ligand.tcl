
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/3LII.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_7_3LII/AChE_7_3LII.pdb
quit
