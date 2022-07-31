#!/bin/sh
if [ $# -ne 2 ]; then
        echo "usage: ./watch.sh \"<file1> <file2> <file3>\",.. <command>"
        exit 1
fi

files=$1
command=$2

echo "watching $files"
echo "execute $command"

last=`ls --full-time $files | awk '{print $6"-"$7}'`
while true; do
        sleep 1
        current=`ls --full-time $files | awk '{print $6"-"$7}'`
        if [ "$last" != "$current" ] ; then
                echo ""
                echo "updated: $current"
                last=$current
                eval $2
        fi
done
