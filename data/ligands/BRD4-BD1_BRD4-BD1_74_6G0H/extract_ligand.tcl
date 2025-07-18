
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6G0H.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_74_6G0H/BRD4-BD1_BRD4-BD1_74_6G0H.pdb
quit
