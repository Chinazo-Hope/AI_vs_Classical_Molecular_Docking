
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5HF5.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_62_5HF5/AChE_62_5HF5.pdb
quit
