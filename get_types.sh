echo -e "\nTYPES \n__________"
grep type schema.graphql |egrep -v 'Mutation|Query|Get|List|Search|Put|type:|Notifi'|awk '{print $2}'

echo -e "\nQUERIES \n__________"
egrep 'Search|Get|List' schema.graphql|gsed -r -e 's/^\s*//g' -e 's/\(.*//g'|egrep -v ':'

echo -e "\nMUTATIONS \n__________"
egrep 'Put|Delete|Add|Remove' schema.graphql| gsed -r -e 's/^\s*//g' -e 's/\(.*//g'|egrep -v ':'

