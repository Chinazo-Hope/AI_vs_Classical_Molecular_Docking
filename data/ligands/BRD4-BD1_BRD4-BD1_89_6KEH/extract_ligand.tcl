
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6KEH.pdb
set sel [atomselect top "resname FMT and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_89_6KEH/BRD4-BD1_BRD4-BD1_89_6KEH.pdb
quit
