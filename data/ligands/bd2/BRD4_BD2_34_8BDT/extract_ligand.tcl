
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8BDT.pdb
set sel [atomselect top "resname QLX and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_34_8BDT/BRD4_BD2_34_8BDT.pdb
quit
