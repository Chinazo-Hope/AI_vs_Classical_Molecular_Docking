
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6ZCI.pdb
set sel [atomselect top "resname QFN and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_56_6ZCI/BRD4-BD1_BRD4-BD1_56_6ZCI.pdb
quit
