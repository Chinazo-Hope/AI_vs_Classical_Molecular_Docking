
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7W3D.pdb
set sel [atomselect top "resname 89T and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_98_7W3D/BRD4-BD1_BRD4-BD1_98_7W3D.pdb
quit
