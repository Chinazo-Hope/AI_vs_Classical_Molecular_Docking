
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5VZS.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_50_5VZS/BRD4-BD1_BRD4-BD1_50_5VZS.pdb
quit
