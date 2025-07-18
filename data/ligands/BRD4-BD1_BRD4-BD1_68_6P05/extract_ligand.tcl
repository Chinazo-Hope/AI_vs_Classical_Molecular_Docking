
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6P05.pdb
set sel [atomselect top "resname GOL and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_68_6P05/BRD4-BD1_BRD4-BD1_68_6P05.pdb
quit
