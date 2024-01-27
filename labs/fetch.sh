#!/bin/bash

if [ -z $1 ]
then
echo Missing args.
exit
fi

echo Will download https://inst.eecs.berkeley.edu/~cs61a/fa23/lab/${1}/${1}.zip
wget "https://inst.eecs.berkeley.edu/~cs61a/fa23/lab/${1}/${1}.zip"
if [ $? -ne 0 ]; then
echo Download error
exit
fi

unzip ${1}.zip
rm ${1}.zip