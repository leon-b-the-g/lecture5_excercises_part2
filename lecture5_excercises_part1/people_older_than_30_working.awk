awk '{
FS="\t" ;
if($6 <= 1989)
{if (NF == 7)
{print $0 ; }}
}' example_people_data.tsv | wc -l

