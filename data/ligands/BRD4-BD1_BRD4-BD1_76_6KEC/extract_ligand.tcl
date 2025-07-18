
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6KEC.pdb
set sel [atomselect top "resname FMT and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_76_6KEC/BRD4-BD1_BRD4-BD1_76_6KEC.pdb
quit
