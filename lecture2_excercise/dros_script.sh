#!/bin/bash

for x in {a..z}; do

 echo "Processing letter $x"
 egrep -o 'D. '$x'\S+' dros_list.txt > $x'_species.txt'

done


