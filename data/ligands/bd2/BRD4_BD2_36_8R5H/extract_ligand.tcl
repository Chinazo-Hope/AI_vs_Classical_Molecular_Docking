
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8R5H.pdb
set sel [atomselect top "resname SY8 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_36_8R5H/BRD4_BD2_36_8R5H.pdb
quit
