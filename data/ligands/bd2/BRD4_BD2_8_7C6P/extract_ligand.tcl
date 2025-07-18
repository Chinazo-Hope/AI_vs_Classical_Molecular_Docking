
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/7C6P.pdb
set sel [atomselect top "resname SQH and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_8_7C6P/BRD4_BD2_8_7C6P.pdb
quit
