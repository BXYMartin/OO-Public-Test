#!/bin/bash
cd ~/Documents/BUAA/WSP/
rm result.txt
if [ ! -f "running" ]; then
	touch "running"
	if [ ! -d "./test_path" ]; then
		echo -e "\033[31mDependency Directory test_path Not Found!\033[0m"
		exit 1
	fi
	echo -e "\033[34mStarting UML Autotest...\033[0m"
	cd test_path
	./test.sh $*
else
	echo "Already Running!"
	cd ./test_path
	git pull
	python failed.py
        git add docs
        git commit -m "Server Experienced a Recent Unsuccessful Check!"
        git push
fi
