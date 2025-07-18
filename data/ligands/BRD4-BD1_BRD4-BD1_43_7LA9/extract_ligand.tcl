
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7LA9.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_43_7LA9/BRD4-BD1_BRD4-BD1_43_7LA9.pdb
quit
