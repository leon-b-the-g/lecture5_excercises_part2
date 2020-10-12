cat awk_file_people | awk '{
if (NF == 7)
{print $0;}
}' | wc -l

echo -e "script is complete"

