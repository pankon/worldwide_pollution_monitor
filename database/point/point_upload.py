#!/usr/bin/env python

#point_upload.py

import os
import sys
import datetime
import json
from sqlalchemy import metadata
from static_config import environment_variables, write_vars

if __name__ == "__main__":
    in_dict = {}
    for arg in sys.argv[1:]:
        key, value = arg.split(':')
        in_dict[key] = value
    in_dict['datetime'] = str(datetime.datetime.now())
    print(json.dumps(in_dict))
