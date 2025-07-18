
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6O5V.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/ache/AChE_21_6O5V/AChE_21_6O5V.pdb
quit
