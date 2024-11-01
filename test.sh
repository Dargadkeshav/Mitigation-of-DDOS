#!/bin/bash

while true
do 
packet=$(shuf -i 10-20 -n 1)
bytes=$(shuf -i 150-200 -n 1)
pause=$(shuf -i 1-5 -n 1)
hping3 -c $packet -d $bytes -s 80 -k 10.0.0.21
sleep $pause
done
