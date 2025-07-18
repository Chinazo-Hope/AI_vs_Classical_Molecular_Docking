
mol new /Users/chinazoemeh/HopeMScP/data/pdb_files/8BDX.pdb
set sel [atomselect top "resname QIY and not water"]
$sel writepdb /Users/chinazoemeh/HopeMScP/data/ligands/bd2/BRD4_BD2_35_8BDX/BRD4_BD2_35_8BDX.pdb
quit
