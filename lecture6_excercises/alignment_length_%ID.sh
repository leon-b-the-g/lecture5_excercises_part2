#!/bin/bash
#A programme to output a list of the alignment lengths and percent ID for all HSPs
match=0
IFS=$'\t'
while read query_acc subject_acc percent_identity alignment_length mismatches gap_opens q_start q_end s_start s_end evalue bit_score
do

#need if statement to exclude lines that start with a #
if test ${query_acc:0:1} != '#';
 then
#here we exclude all lines starting with a # from being contributed to the output
  if [[ ${mismatches} -gt 20 ]];
   then
    match=$((match+1));
  #This counts the line the programme is on
    echo -e "${match}\t${subject_acc}\t${percent_identity}\t${alignment_length}"
  fi #closes mismatches greater than 20 if statement
fi
done < blastoutput2.out | more
