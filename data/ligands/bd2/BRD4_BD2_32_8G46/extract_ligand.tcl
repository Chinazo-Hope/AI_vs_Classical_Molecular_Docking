
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8G46.pdb
set sel [atomselect top "resname YK3 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_32_8G46/BRD4_BD2_32_8G46.pdb
quit
