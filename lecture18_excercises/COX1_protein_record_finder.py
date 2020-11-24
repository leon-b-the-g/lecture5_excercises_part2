#!/usr/bin/python3

from Bio import Entrez
from Bio import SeqIO
import os
Entrez.email = "s1757725@ed.ac.uk"
my_search_fasta = Entrez.esearch(db="protein",term="Mammalia COX1 complete",rettype="fasta", retmode="text")

fasta_result = Entrez.read(my_search_fasta)
print (fasta_result)
search_count = len(list(fasta_result["IdList"]))
print (search_count)
#fasta_result["IdList"]

for accession in fasta_result['IdList']:
    fasta = Entrez.efetch(db="protein",id=accession,rettype="fasta")
    record = SeqIO.read(fasta, "fasta")
    print("COX1",record.description)

