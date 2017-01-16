#!/usr/bin/env python

#process_input.py

import os
import sys
import datetime
import json
from static_config import environment_variables, write_vars

if __name__ == "__main__":
    in_dict = {}
    for arg in sys.argv[1:]:
        key, value = arg.split(':')
        in_dict[key] = value
    in_dict['datetime'] = str(datetime.datetime.now())
    print(json.dumps(in_dict))
    file_name = "cache-"+'_-_'.join(in_dict[key] for key in environment_variables)
    open_type = 'a'
    if not os.path.isfile(file_name):
        open_type = 'w'
    with open(file_name, open_type) as f:
        f.write(json.dumps(dict((
            (key, in_dict[key])
            for key in write_vars
        ))))
        f.write('\n')
