
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6WVP.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_53_6WVP/AChE_53_6WVP.pdb
quit
