
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6NTG.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_42_6NTG/AChE_42_6NTG.pdb
quit
