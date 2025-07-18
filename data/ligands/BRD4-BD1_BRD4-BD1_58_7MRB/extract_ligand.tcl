
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7MRB.pdb
set sel [atomselect top "resname N49 and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_58_7MRB/BRD4-BD1_BRD4-BD1_58_7MRB.pdb
quit
