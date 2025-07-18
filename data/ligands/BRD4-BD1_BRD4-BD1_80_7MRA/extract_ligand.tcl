
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7MRA.pdb
set sel [atomselect top "resname ZMJ and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_80_7MRA/BRD4-BD1_BRD4-BD1_80_7MRA.pdb
quit
