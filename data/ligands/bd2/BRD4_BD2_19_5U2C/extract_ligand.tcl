
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5U2C.pdb
set sel [atomselect top "resname 82Y and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_19_5U2C/BRD4_BD2_19_5U2C.pdb
quit
