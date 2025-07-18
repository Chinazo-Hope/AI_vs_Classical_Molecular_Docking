
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5HF8.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_63_5HF8/AChE_63_5HF8.pdb
quit
