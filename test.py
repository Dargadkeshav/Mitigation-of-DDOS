#!/usr/bin/env python3

import csv
i=0
with open("C:\Users\ASUS\Downloads\project.zip\project\Data.csv") as t1:
    while(i>3000):
        for line in t1.readline():
            if (i==2762):
                print(line)
            i+=1
            print(i)
