
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7KO0.pdb
set sel [atomselect top "resname 5W2 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_30_7KO0/BRD4_BD2_30_7KO0.pdb
quit
