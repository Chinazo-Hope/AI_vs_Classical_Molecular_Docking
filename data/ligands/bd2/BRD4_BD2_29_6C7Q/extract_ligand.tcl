
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6C7Q.pdb
set sel [atomselect top "resname CME and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_29_6C7Q/BRD4_BD2_29_6C7Q.pdb
quit
