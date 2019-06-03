#!/bin/bash

if [ ! -d "gen_case" ]; then
    mkdir gen_case
else
    rm -rf gen_case
    mkdir gen_case
fi

for file in $(ls "./test_mdj")
do
    echo -e "[i]  INFO:\t Generating Tests for $file"
    list=$(java -jar uml.jar list -s "./test_mdj/$file")
    for model in $(python model.py "$list")
    do
        content=$(java -jar uml.jar dump -s "./test_mdj/$file" -n "$model")
        for ((i=1;i<=5;i++))
        do
            echo "$content" >> "./gen_case/"$file"_"$model"_"$i".test"
            echo "END_OF_MODEL" >> "./gen_case/"$file"_"$model"_"$i".test"
            python gen.py "$content" >> "./gen_case/"$file"_"$model"_"$i".test"
        done
    done

done
