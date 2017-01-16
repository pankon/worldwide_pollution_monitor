#!/usr/bin/env python

# commit_data.py

import os
import sys

def commit_data():
    for file in os.popen('ls | grep cache-*'):
        print(file)
    print(os.popen('ls | grep cache-*'))

if __name__ == "__main__":
    commit_data()
