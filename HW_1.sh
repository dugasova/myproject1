#!/bin/bash
echo $1
mkdir -p $1
cd $1
mkdir test1 test2 test3
cd test1
touch file{1..3}.txt file{1..2}.json
mkdir folder1 folder2 folder3
ls -la
mv *.json ./folder3/


