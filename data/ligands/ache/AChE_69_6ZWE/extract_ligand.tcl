
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6ZWE.pdb
set sel [atomselect top "resname NAG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_69_6ZWE/AChE_69_6ZWE.pdb
quit
