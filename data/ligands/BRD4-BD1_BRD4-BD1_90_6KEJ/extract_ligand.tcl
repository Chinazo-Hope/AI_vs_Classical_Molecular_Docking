
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6KEJ.pdb
set sel [atomselect top "resname FMT and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_90_6KEJ/BRD4-BD1_BRD4-BD1_90_6KEJ.pdb
quit
