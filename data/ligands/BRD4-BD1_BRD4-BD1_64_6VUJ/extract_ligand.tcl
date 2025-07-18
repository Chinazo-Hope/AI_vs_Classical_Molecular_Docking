
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6VUJ.pdb
set sel [atomselect top "resname NO3 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_64_6VUJ/BRD4-BD1_BRD4-BD1_64_6VUJ.pdb
quit
