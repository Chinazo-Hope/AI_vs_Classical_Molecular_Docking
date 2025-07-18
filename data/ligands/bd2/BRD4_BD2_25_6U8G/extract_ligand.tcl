
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U8G.pdb
set sel [atomselect top "resname ALY and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_25_6U8G/BRD4_BD2_25_6U8G.pdb
quit
