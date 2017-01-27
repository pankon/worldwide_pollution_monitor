#!/usr/bin/env python

#point_upload.py

import os
import sys
import datetime
import json
from create.setup_databases import Point, create_engine
from static_config import environment_variables, write_vars

if __name__ == "__main__":
    in_dict = {}
    for arg in sys.argv[1:]:
        key, value = arg.split(':')
        in_dict[key] = value
    in_dict['datetime'] = str(datetime.datetime.now())
    #json.dumps(in_dict)
    engine = create_engine('sqlite3:///')
    Point.create(engine)
    a = Point(*in_dict)
    a.insert()
