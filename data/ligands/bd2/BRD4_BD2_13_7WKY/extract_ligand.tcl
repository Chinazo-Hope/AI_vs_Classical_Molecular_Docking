
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7WKY.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_13_7WKY/BRD4_BD2_13_7WKY.pdb
quit
