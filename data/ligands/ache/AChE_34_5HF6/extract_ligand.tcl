
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5HF6.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_34_5HF6/AChE_34_5HF6.pdb
quit
