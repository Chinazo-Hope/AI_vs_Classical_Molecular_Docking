
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7L9M.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_45_7L9M/BRD4-BD1_BRD4-BD1_45_7L9M.pdb
quit
