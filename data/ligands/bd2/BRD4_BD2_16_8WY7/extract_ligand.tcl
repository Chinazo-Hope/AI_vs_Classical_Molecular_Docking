
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8WY7.pdb
set sel [atomselect top "resname XHN and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_16_8WY7/BRD4_BD2_16_8WY7.pdb
quit
