
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7USK.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_21_7USK/BRD4_BD2_21_7USK.pdb
quit
