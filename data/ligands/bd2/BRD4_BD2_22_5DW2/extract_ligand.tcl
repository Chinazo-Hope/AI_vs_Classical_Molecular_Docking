
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5DW2.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_22_5DW2/BRD4_BD2_22_5DW2.pdb
quit
