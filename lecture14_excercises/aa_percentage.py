#!/usr/bin/python3
#Input: argument 1: protein sequence , arguement 2: a.a. residue
#Process count arguement 2 in arguement 1. 
	#Divide length of arguement 1 by the count
#Output
	#Return the result of the calculation (NOT rounded, since this is included in the assert statements

def aa_percent(sequence,residue):
	a_in_seq = sequence.upper().count(residue.upper())
	length = len(sequence)
	percentage = (a_in_seq/length) * 100
	return percentage

assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
