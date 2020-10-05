NAMES=$(egrep '^\s[a-z]' schema.graphql |cut -d: -f1|gsed 's/^\s*//g'|egrep '[a-z]*[A-Z]+'|grep -v \(| sort|uniq)
for newname in $NAMES; do
	first_half=$(echo $newname|egrep -o '^[a-z]*')
	second_half=$(echo $newname|egrep -o '[A-Z]+.*'|tr '[:upper:]' '[:lower:]')
	# echo "FIRST_HALF: $first_half"
	# echo "SECOND_HALF: $second_half"
	old_name="${first_half}_${second_half}"
	for f in $(find ./response_templates -type f); do
		gsed -ri "s/$old_name/$newname/g" $f|grep $newname
	done;
done
