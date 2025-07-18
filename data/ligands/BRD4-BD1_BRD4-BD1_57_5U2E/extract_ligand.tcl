
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5U2E.pdb
set sel [atomselect top "resname 837 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_57_5U2E/BRD4-BD1_BRD4-BD1_57_5U2E.pdb
quit
