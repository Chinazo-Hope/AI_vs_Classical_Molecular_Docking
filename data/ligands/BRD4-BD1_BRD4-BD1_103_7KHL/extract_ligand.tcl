
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7KHL.pdb
set sel [atomselect top "resname WEM and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_103_7KHL/BRD4-BD1_BRD4-BD1_103_7KHL.pdb
quit
