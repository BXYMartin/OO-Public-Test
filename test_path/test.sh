#!/bin/bash
git pull
echo -e "\033[33m\c"
test_dir="./test_case/"
if [ $# == 1 ];
then
    test_dir="./gen_case/"
fi
if [ $# == 2 ];
then
    test_dir="./gen_case/"
    bash gen.sh
fi
s="Success"
record=0
for file in $(ls $test_dir)
do
    name=$test_dir$file
    catch=$(rm -rf ./runtime)
    mkdir runtime
    touch ./runtime/error.res
    echo "[^] Running Test On $file"
    cat "$name" | python comm.py
    result=$(python comp.py)
    ans=$?
    if [ $ans == 0 ];
    then
        echo -e "\033[0m\033[32m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m"
        echo -e "\033[32m[*] SUCCESS:\t $file\033[0m"
        echo -e "\033[34m\c"
        echo "$result"
        echo -e "\033[0m\c"
        echo -e "\033[33m<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    else
        record=$[$record+1]
        if [ $record -gt 3 ];
        then
            break
        fi
        echo -e "\033[31m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\033[0m"
        echo -e "\033[5;31m[!] ERROR:\t UML Checker Failure!\033[0m"
        echo -e "\033[31m\c"
        echo "$result"
        echo -e "\033[0m\c"
        echo -e "\033[34m\c"
        cd docs/_posts
        git checkout master
        git pull
        cd ../../
        i=$(cat "$name")
        info=$(python info.py "$name" $ans "$result" "$file" "$i")
        echo $info
        echo -e "\033[0m\c"
        errors=$(cat "./runtime/error.res")
        echo $errors
        for del in $errors
        do
            curl -X POST -H "Authorization: token faaa3c3b7a81a8c9e9b818951c74cfa6ff99745b" -i -d '{"title":"Runtime Error For '"$del"'","body":"'"$info"'","assignee":"'"$del"'"}' https://api.github.com/repos/BXYMartin/OO-Public/issues
            git rm "./test_jar/$del"
        done
        cd docs/_posts
        git add .
        git commit -m "Add Error File"
        git push
        cd ../../
        git add docs/_posts
        git commit -m "Wrong Behaviour Detected!"
        git push
        s="Failure"
        #break
    fi
done
echo -e "\033[0m\c"
cd docs/_posts
git checkout master
git pull
cd ../../
all=$(ls ./test_jar/)
mmm=$(ls ./test_mdj/)
python success.py "$all" "$mmm" "$s"
cd docs/_posts
git add .
git commit -m "Add Error File"
git push
cd ../../
git add docs/_posts
git commit -m "Finished!"
git push
rm ../running
