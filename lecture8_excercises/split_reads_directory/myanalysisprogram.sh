#!/usr/bin/bash

myfavseq="CATAAAACATCAAAGTGAACAGATTGTAGTGTAAGAAGTTAGATTAA"
while read line
do read sequence_under_line 
 if [[ $sequence__under_line == *$myfavseq* ]];
 then
  echo "The sequence was found in" $line $sequence_under_line
 fi 
done <$1
#$1 is a variable which has values reassigned to it every time the eddie submission script runs this script.


