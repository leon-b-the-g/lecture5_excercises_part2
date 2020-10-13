esearch -db nucleotide -query "Mimosa+Pudica[organism]" | efetch -db nucleotide -format fasta > Mimosa_Pudica.nuc.fa
#In the query it is important to format the search correctly. Here, a + sign means a " " (space).
#You can use any format that NCBI supports for the -format flag input. 

