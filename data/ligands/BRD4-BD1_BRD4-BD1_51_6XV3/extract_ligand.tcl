
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6XV3.pdb
set sel [atomselect top "resname O2B and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_51_6XV3/BRD4-BD1_BRD4-BD1_51_6XV3.pdb
quit
