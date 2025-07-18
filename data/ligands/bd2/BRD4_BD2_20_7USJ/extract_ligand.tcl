
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7USJ.pdb
set sel [atomselect top "resname 82V and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_20_7USJ/BRD4_BD2_20_7USJ.pdb
quit
