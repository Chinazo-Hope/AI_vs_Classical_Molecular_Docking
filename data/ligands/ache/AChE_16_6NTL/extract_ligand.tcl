
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6NTL.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_16_6NTL/AChE_16_6NTL.pdb
quit
