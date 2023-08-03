#!/usr/bin/python3
for i in range(10):
    for j in range(i+i, 10):
        print("{:d}{:d}".format(i, j), end=', ' if i < 9 else '\n')
