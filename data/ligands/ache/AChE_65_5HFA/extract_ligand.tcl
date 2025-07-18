
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5HFA.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_65_5HFA/AChE_65_5HFA.pdb
quit
