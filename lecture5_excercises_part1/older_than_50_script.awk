egrep "Mozambique" example_people_data.tsv | awk '{
#The egrep takes all the listings from Mozambique and outputs them into the awk
FS="\t" ;
{if ($6 <=1970);
{print $1 " is born in " $6 " and is from " $7 "."; }
}
}' 
#This awk goes through the lists and prints any listing older than 1970

