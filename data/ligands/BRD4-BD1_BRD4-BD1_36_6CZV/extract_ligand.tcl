
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6CZV.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_36_6CZV/BRD4-BD1_BRD4-BD1_36_6CZV.pdb
quit
