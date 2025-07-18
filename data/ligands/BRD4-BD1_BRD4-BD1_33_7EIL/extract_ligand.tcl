
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7EIL.pdb
set sel [atomselect top "resname 909 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_33_7EIL/BRD4-BD1_BRD4-BD1_33_7EIL.pdb
quit
