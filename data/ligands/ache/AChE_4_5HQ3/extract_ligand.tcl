
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5HQ3.pdb
set sel [atomselect top "resname VX and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_4_5HQ3/AChE_4_5HQ3.pdb
quit
