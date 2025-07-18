
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6V1K.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_69_6V1K/BRD4-BD1_BRD4-BD1_69_6V1K.pdb
quit
