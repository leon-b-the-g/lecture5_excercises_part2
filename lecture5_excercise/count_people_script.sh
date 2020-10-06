#script to count number of people in people data file
IFS="\t";
while read $number_of_people
do
cat example_people_data.tsv | wc -l > $number_of_people;

echo -e "There are "$number_of_people" listed in this file."

done < example_people_data.tsv
