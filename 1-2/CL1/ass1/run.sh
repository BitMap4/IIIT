#!/bin/bash
for i in {1,2,3,4} 
do
    echo "Running task $i"
    if command -v python3 &>/dev/null; then
        python3 Task_$i/code.py
    else
        python Task_$i/code.py
    fi
done