#!/usr/bin/python3
#Input: argument 1: protein sequence , arguement 2: a.a. residue
#Process:
	# a for loop that goes through the lsit of amino acids and counts the amount of times the given amino acids shows in arguemnt 1. Then, the amount should be added to a variable that totals the times the amino acids occured. 
	#Divide length of arguement 1 by the total variable
#Output
	#Return the result of the calculation (NOT rounded, since this is included in the assert statements

def aa_list_percent(sequence,residue=["A","I","L","M","F","W","Y","V"]):
	total = 0
	for aa in residue:
		freq = sequence.upper().count(aa.upper())
		total = total + freq
	#print ("The total is" + str(total))
	length = len(sequence)
	percentage = (total/length) * 100
	return percentage


assert round(aa_list_percent("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(aa_list_percent("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(aa_list_percent("MSRSLLLRFLLFLLLLPPLP")) == 65

