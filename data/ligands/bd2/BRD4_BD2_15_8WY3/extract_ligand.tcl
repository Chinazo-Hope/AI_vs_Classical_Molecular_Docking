
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8WY3.pdb
set sel [atomselect top "resname XHE and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_15_8WY3/BRD4_BD2_15_8WY3.pdb
quit
