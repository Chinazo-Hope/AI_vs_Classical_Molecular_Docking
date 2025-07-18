
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6NTM.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_45_6NTM/AChE_45_6NTM.pdb
quit
