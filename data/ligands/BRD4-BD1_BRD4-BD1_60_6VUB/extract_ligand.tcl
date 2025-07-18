
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6VUB.pdb
set sel [atomselect top "resname RLG and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_60_6VUB/BRD4-BD1_BRD4-BD1_60_6VUB.pdb
quit
