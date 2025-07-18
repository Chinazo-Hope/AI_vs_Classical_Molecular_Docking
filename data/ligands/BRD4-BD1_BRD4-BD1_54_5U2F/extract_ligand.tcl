
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5U2F.pdb
set sel [atomselect top "resname 82Y and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_54_5U2F/BRD4-BD1_BRD4-BD1_54_5U2F.pdb
quit
