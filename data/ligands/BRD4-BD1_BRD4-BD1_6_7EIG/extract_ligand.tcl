
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7EIG.pdb
set sel [atomselect top "resname N03 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_6_7EIG/BRD4-BD1_BRD4-BD1_6_7EIG.pdb
quit
