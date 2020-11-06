#!/usr/bin/python3
#Input: argument 1: protein sequence , threshold of undetermined bases
#Process:
	# a for loop that goes through the seqeuence and counts how many bases are not ATGC 
	# A statement that assesses whether the for loop output is greater than the threshold or smaller than the threshold
#Output
	#Returns the result of the evaluation (TRUE or FALSE)


def base_count(sequence,threshold):
	seq_up	= sequence.upper()
	count = 0
	for base in seq_up:
		if base not in ["A", "T", "G", "C"]:
			count = count + 1
		#print ("hi, this is the count:",count)
	percent_count = count/ len(seq_up)
	evaluation = percent_count >= threshold
	#print (evaluation)
	return evaluation

#If seqeuence has more percentage unknown bases than the threshold then True, otherwise False
assert base_count("ATGCATGCATGC", 0.4) == False
assert base_count("ATGCATGCATGC", 0) == True
assert base_count("ATGCATGCATGCWHOOOOOOOOPPPPPPPPPPppp", 0.4) == True
assert base_count("ATGCATGCATGCWHOOOOOOOOPPPPPPP", 0.90) == False
