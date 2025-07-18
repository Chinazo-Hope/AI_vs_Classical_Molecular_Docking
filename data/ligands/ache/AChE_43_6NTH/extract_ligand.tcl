
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6NTH.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_43_6NTH/AChE_43_6NTH.pdb
quit
