
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6O5S.pdb
set sel [atomselect top "resname VX and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_20_6O5S/AChE_20_6O5S.pdb
quit
