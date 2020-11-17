#!/usr/bin/python3

#A script that uses the code explained in the lecture to:
	#1. Use the ecoli.txt file and, using the code above as a starting point, make a chart which shows the AT content in a sliding window.
	#The alignment.txt file contains a multiple sequence alignment, one sequence per line. We want to draw a plot of protein conservation based on the alignment similarities, but without using plotcon!
import os, sys, shutil
import numpy as np
import matplotlib.pyplot as plt 

#The code will have to
#1 read in the data
#2 get each coloumn in turn
#3 measure the conservation at each column 
	#what proportion of aa residues are the same
#4 append the measurement to a list
#draw the chart 

#Copying the files I need for the excercise
#WORKS hashed out to save time
#shutil.copy ("/localdisk/data/BPSM/Lecture17_AI/ecoli.txt","ecoli.txt")

#shutil.copy ("/localdisk/data/BPSM/Lecture17_AI/alignment.txt","alignment.txt")

#os.system ("ls -hl")

ecoli=  open("ecoli.txt").read().replace("\n","")[0:100000]
#print (ecoli)
window= 10000
AT = []
for start in range(len(ecoli) - window):
	win = ecoli [start:start+window]
	#print (win)
	AT.append(win.count("AT") / window)

plt.figure(figsize=(20,10))
plt.plot(AT, label="AT",linewidth=3)
plt.ylabel('Fraction of bases')
plt.xlabel('Position on genome')
plt.title("AT frequency E coli genome")
plt.legend()
plt.savefig("Chart_16A.png",transparent=True)
plt.show()

