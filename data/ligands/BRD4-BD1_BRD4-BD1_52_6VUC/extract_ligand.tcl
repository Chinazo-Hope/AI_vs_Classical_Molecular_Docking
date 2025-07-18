
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6VUC.pdb
set sel [atomselect top "resname RLS and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_52_6VUC/BRD4-BD1_BRD4-BD1_52_6VUC.pdb
quit
