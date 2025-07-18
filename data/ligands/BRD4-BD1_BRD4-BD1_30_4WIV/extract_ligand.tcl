
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/4WIV.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_30_4WIV/BRD4-BD1_BRD4-BD1_30_4WIV.pdb
quit
