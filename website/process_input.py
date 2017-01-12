#!/usr/bin/env python

#process_input.py

import sys
import datetime
import json

if __name__ == "__main__":
    dIn = {}
    for arg in sys.argv[1:]:
        key, value = arg.split(':')
        dIn[key] = value
    dIn['datetime'] = str(datetime.datetime.now())
    print(json.dumps(dIn))
