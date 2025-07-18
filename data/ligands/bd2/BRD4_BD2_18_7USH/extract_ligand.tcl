
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7USH.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_18_7USH/BRD4_BD2_18_7USH.pdb
quit
