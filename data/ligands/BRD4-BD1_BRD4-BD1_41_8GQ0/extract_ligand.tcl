
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8GQ0.pdb
set sel [atomselect top "resname FMT and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_41_8GQ0/BRD4-BD1_BRD4-BD1_41_8GQ0.pdb
quit
