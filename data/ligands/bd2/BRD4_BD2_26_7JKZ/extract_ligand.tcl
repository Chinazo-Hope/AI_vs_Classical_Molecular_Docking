
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7JKZ.pdb
set sel [atomselect top "resname YF6 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_26_7JKZ/BRD4_BD2_26_7JKZ.pdb
quit
