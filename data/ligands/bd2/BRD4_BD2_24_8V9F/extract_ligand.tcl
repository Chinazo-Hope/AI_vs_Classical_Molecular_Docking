
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8V9F.pdb
set sel [atomselect top "resname YPB and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_24_8V9F/BRD4_BD2_24_8V9F.pdb
quit
