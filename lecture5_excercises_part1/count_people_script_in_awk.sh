cat awk_file_people | awk '{
if (NF == 7);
#if number of fields is equal to 7
{print $0;}
#print the first line 
}' | wc -l
#word count at the end
echo -e "script is complete"

