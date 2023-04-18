#!/bin/sh
# Runs pytest watcher and then flake8 after a pass
while :; do
   pytest
   if [ $? -eq 0 ]; then
      flake8
   fi
   date
   watch -n1 -g find . -type f -ls > /dev/null 2>&1
done