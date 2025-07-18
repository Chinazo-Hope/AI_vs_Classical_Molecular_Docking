
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5M3A.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_82_5M3A/BRD4-BD1_BRD4-BD1_82_5M3A.pdb
quit
