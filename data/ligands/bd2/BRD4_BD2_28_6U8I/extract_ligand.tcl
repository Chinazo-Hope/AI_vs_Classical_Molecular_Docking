
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/6U8I.pdb
set sel [atomselect top "resname ACE and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_28_6U8I/BRD4_BD2_28_6U8I.pdb
quit
