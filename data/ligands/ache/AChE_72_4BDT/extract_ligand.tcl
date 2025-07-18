
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/4BDT.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_72_4BDT/AChE_72_4BDT.pdb
quit
