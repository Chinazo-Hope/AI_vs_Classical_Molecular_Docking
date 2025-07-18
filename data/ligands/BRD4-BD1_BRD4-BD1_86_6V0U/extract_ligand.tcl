
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6V0U.pdb
set sel [atomselect top "resname BMF and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_86_6V0U/BRD4-BD1_BRD4-BD1_86_6V0U.pdb
quit
