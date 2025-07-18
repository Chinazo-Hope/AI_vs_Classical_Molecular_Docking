
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6PSB.pdb
set sel [atomselect top "resname Y18 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_96_6PSB/BRD4-BD1_BRD4-BD1_96_6PSB.pdb
quit
