
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7USG.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_17_7USG/BRD4_BD2_17_7USG.pdb
quit
