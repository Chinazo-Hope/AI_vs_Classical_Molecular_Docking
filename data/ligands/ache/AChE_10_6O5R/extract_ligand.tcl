
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6O5R.pdb
set sel [atomselect top "resname LND and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_10_6O5R/AChE_10_6O5R.pdb
quit
