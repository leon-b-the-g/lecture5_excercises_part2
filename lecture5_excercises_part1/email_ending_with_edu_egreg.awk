#code to list names in reverse alphabetical order
 cut -f2 example_people_data.tsv | \
 grep '\.edu' | \
# greps all LINES ending in .edu	You have to but the backslash since just a "." means "preceeding characters match any amount of times.
 sort -k7,7 -k1,1r 
#sort line 7,position 7 (country) then sort line 1, postion 1 in reverse order


