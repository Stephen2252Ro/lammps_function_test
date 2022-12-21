First, run the in.mkcombine script:
lmp -in in.mkcombine
The *.chunk.txt files contain the atom number for each chunk (layer ID, bin ID, etc.). Check them and make sure the numbers look OK.
Finally, convert the dump files into atomfile format via the dump2atomfile.bash script:
./dump2atomfile.bash 10x10p5w2.5d2.5.binID.dump.txt > table.atomfile.binID
./dump2atomfile.bash 10x10p5w2.5d2.5.layerID.dump.txt > table.atomfile.layerID
./dump2atomfile.bash 10x10p5w2.5d2.5.xi.dump.txt > table.atomfile.xi
