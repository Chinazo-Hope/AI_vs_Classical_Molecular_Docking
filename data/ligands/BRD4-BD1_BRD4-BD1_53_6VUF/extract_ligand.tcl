
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6VUF.pdb
set sel [atomselect top "resname RLV and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/BRD4-BD1_BRD4-BD1_53_6VUF/BRD4-BD1_BRD4-BD1_53_6VUF.pdb
quit
