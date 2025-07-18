
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6KEK.pdb
set sel [atomselect top "resname FMT and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_91_6KEK/BRD4-BD1_BRD4-BD1_91_6KEK.pdb
quit
