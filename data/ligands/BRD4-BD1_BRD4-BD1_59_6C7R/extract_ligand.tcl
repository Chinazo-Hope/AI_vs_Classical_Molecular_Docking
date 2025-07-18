
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6C7R.pdb
set sel [atomselect top "resname EO4 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_59_6C7R/BRD4-BD1_BRD4-BD1_59_6C7R.pdb
quit
