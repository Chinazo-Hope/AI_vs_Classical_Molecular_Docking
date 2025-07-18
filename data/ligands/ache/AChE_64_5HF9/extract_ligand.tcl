
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5HF9.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_64_5HF9/AChE_64_5HF9.pdb
quit
