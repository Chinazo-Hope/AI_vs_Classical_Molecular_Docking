
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U6L.pdb
set sel [atomselect top "resname ALY and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_27_6U6L/BRD4_BD2_27_6U6L.pdb
quit
