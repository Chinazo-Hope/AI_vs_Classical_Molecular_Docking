
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7AQT.pdb
set sel [atomselect top "resname EAM and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_4_7AQT/BRD4_BD2_4_7AQT.pdb
quit
