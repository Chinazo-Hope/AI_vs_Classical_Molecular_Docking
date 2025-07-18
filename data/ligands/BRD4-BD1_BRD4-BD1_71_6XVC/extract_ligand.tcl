
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6XVC.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_71_6XVC/BRD4-BD1_BRD4-BD1_71_6XVC.pdb
quit
