#!/usr/bin/python3

import os
import re
#First, make a variable containing the data
og_accessions = "xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp"
#Now make varibale into a list and remove the spaces found in some elements
accessions_list = og_accessions.replace(" ", "").split(",",)


print (accessions_list)

#This is a for loop that searches the list for accessions containing the number 5
for element in accessions_list:
	search1=re.search(r".5.",element)
	if search1:
		print ("This accession contained the number 5:",element)
	else:
		continue
#This for loop searches for accessions containing d or e
for element in accessions_list:
	search1=re.search(r".d.|.e.",element)
	if search1:
		print ("This accession contained d or e:",element)
	else:
		continue

#This for loop searches for accessions containing d or e in that order with a single letter in between
for element in accessions_list:
	search1=re.search(r"[d].[e]",element)
	if search1:
		print ("This accession contained d and e seperated by 1 character:",element)
	else:
		continue

#This for loop searches for accessions containing d and e in any order
for element in accessions_list:
	search1=re.search(r"(de)|(ed)",element)
	if search1:
		print ("This accession contained d and e in any order:",element)
	else:
		continue

#This for loop searches for accessions starting with x or y
for element in accessions_list:
	search1=re.search(r"^x|^y",element)
	if search1:
		print ("This accession started with x or y:",element)
	else:
		continue

#This for loop searches for accessions starting with x or y and ended with e
for element in accessions_list:
	search1=re.search(r"[^x|^y][e]{1}$",element)
	if search1:
		print ("This accession started with x or y and ended with e:",element)
	else:
		continue

#This for loop searches for accessions containing 3 numbers in any order
#Need to use special character \d
for element in accessions_list:
	if len(re.findall(r"\d",element)) == 3:
		print ("This accession contained 3 numbers in any order:",element)
	else:
		continue

#This for loop searches for accessions starting with x or y and ended with e
for element in accessions_list:
	search1=re.search(r"\d{3,}",element)
	if search1:
		print ("This accession had 3 digits in a row:",element)
	else:
		continue
