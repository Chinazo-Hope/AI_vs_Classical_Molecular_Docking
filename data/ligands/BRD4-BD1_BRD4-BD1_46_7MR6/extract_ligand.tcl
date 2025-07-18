
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7MR6.pdb
set sel [atomselect top "resname ZMV and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_46_7MR6/BRD4-BD1_BRD4-BD1_46_7MR6.pdb
quit
