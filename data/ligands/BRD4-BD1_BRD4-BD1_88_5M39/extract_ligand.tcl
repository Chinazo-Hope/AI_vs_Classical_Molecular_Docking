
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5M39.pdb
set sel [atomselect top "resname 7EA and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_88_5M39/BRD4-BD1_BRD4-BD1_88_5M39.pdb
quit
