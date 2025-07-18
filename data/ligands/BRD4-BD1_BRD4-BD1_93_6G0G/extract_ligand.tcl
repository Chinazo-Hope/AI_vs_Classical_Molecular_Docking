
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6G0G.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_93_6G0G/BRD4-BD1_BRD4-BD1_93_6G0G.pdb
quit
