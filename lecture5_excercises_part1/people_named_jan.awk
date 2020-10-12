awk '{
FS="\t" ;
{if ($1 == "Jan")
#if the name field is equal to Jan and can have anythig that follows 
#AND the number of fields is equal to 7
{print $1; }
}
}' example_people_data.tsv | wc -l 

