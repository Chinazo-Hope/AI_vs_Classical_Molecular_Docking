
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7WJS.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_12_7WJS/BRD4_BD2_12_7WJS.pdb
quit
