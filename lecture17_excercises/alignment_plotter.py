#!/usr/bin/python3
#The alignment.txt file contains a multiple sequence alignment, one sequence per line. We want to draw a plot of protein conservation based on the alignment similarities, but without using plotcon!
import os, sys, shutil
import numpy as np
import matplotlib.pyplot as plt


alignment= open("alignment.txt")
aligned_seqs = []
counter = 0

#This checks the length of the alignments. its 2013 consistently
for line in alignment:
	counter += 1
	#print ("Sequence", counter, "was",len(line.rstrip("\n")),"long")
	aligned_seqs.append(line.rstrip("\n"))

alignment_length = len(aligned_seqs[0])
print (alignment_length)
uniques_per_column = []

#This goes through each coloumn in each sequence and if the amino acid in that column is not a "-" it will add it to the list "column". It then makes a non redundant list of column, counts the amount and then adds the resulting "number of uniques" to a new list, each element in this new list representing the number of unique amino acids in each sequence.
for column_number in range(alignment_length):
	column = []
	for seq in aligned_seqs:
		aa = seq[column_number]
		if aa != "-":
			column.append(seq[column_number])
	uniques = len(set(column))
	uniques_per_column.append(uniques)

#This for loop goes through "windows" of the uniques per column list and generates a score pased on the (DONT REALLY UNDERSTAND YET)
window = 10
numbers_to_plot = []
for start in range(len(uniques_per_column) - window):
	win = uniques_per_column[start:start+window]
	score = sum(win) / len(win)
	numbers_to_plot.append(score)


#Plotting the conservation:
plt.figure(figsize=(15,8))
plt.xlim(0,len(numbers_to_plot)) # Uses the count of the unique amino acid numbers 
plt.plot(numbers_to_plot,linewidth=3,color="green")
plt.title('EXERCISE 2')
plt.ylabel('Unique amino acid residues')
plt.xlabel('Residue position')
plt.savefig("Chart_Exercise_2.png",transparent=True)
plt.show()


