
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6G0F.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_73_6G0F/BRD4-BD1_BRD4-BD1_73_6G0F.pdb
quit
