
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/5DW2.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_65_5DW2/BRD4-BD1_BRD4-BD1_65_5DW2.pdb
quit
