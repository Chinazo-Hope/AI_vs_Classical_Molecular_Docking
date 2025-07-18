
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7REL.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_9_7REL/BRD4-BD1_BRD4-BD1_9_7REL.pdb
quit
