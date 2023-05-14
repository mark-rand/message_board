#!/bin/sh

export PYTHONPATH=`pwd`

cleanup() {
    echo "Cleaning stuff up..."
    exit
}

trap cleanup INT TERM

# Runs pytest and then flake8 after a pass
while :; do
   pytest
   if [ $? -eq 0 ]; then
      flake8
      if [ $? -eq 0 ]; then
         echo Formatting all okay
      fi
   fi
   date
   watch -n1 -g "find . -type f -ls | sum" > /dev/null 2>&1
done
