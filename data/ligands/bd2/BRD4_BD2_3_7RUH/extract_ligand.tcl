
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7RUH.pdb
set sel [atomselect top "resname CME and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_3_7RUH/BRD4_BD2_3_7RUH.pdb
quit
