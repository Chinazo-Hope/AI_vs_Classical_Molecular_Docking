
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8V9F.pdb
set sel [atomselect top "resname YPB and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_105_8V9F/BRD4-BD1_BRD4-BD1_105_8V9F.pdb
quit
