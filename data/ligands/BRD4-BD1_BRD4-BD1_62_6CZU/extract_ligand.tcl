
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6CZU.pdb
set sel [atomselect top "resname EDO and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_62_6CZU/BRD4-BD1_BRD4-BD1_62_6CZU.pdb
quit
