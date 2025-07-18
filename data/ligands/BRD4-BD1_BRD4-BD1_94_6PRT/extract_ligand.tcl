
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6PRT.pdb
set sel [atomselect top "resname OWA and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_94_6PRT/BRD4-BD1_BRD4-BD1_94_6PRT.pdb
quit
