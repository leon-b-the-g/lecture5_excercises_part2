#!/usr/bin/python3
import os
#First We have to open the file "input.txt"
#For each line in the file, cut the first 14 base pair fragment
#Output the trimmed fragement to a new file
#Print the length of each adapter-free seqeuence to the screen.

input_file = open("input.txt")

#For loop to cut the fragments of each line
line_n = 0
for line in input_file:
	line_n = (line_n + 1)
	newfile = open("fragment_" + str(line_n) + ".txt", "w")
	newfile.write (line[14:])
	newfile.close ()
	print ("This fragment is " + str(len((line[14:]))) + " long.")

