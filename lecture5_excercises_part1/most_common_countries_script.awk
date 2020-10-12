#script to find out the most common country in descending order
cut -f7 example_people_data.tsv | \
 sort | \
 uniq -c | \
 sort -k1,1nr | \
 head -5 
