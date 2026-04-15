#!/bin/zsh

#uncomment to display commands as they execute:
#set -x

if [ "$#" -ne 2 ]; then
    echo "Error: Incorrect number of arguments." 1>&2
    echo "Usage: $0 dog_ads_filename cat_ads_filename" 1>&2
    exit 1
fi

CATS=$1
DOGS=$2

KEY_PATH="/Users/paul_poling/Desktop/CSA_code/csa-231-pet-food-pcp/TestData"

sort $CATS | uniq > dedupedCats
echo "\nUsers missing from Cats file: \t\t  Usernames in your Cats file that shouldn't be:\n"
diff -y --suppress-common-lines $KEY_PATH/500postsCatKEY.txt <(sed 's/ .*//' dedupedCats)
rm dedupedCats

# Pause until ENTER entered:
#read

sort $DOGS | uniq > dedupedDogs
echo "\n\nUsers missing from Dogs file: \t\t  Usernames in your Dogs file that shouldn't be:\n"
diff -y --suppress-common-lines $KEY_PATH/500postsDogKEY.txt <(sed 's/ .*//' dedupedDogs)
rm dedupedDogs

echo "\n========================================="
echo "\nRequirement: Users receive at most one Dog ad and one Cat ad."

DUPES_D=`sort $DOGS | uniq -d | wc -l`  
DUPES_C=`sort $CATS | uniq -d | wc -l`  

if [ $DUPES_C -gt 0 ]; then
    echo "\nYour $CATS file has $DUPES_C duplicate usernames.  Requirement: Zero duplicates"
fi
if [ $DUPES_D -gt 0 ]; then
    echo "\nYour $DOGS file has $DUPES_D duplicate usernames.  Requirement: Zero duplicates"
fi
if [ $(($DUPES_C + $DUPES_D)) -eq 0 ]; then
     echo "\nGreat job, no duplicates!"
fi
echo "\n"
