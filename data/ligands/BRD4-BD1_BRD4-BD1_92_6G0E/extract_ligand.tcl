
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6G0E.pdb
set sel [atomselect top "resname FMT and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_92_6G0E/BRD4-BD1_BRD4-BD1_92_6G0E.pdb
quit
