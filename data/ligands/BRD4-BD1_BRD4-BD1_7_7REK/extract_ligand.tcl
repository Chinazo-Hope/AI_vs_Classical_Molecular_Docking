
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7REK.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_7_7REK/BRD4-BD1_BRD4-BD1_7_7REK.pdb
quit
