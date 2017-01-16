#!/usr/bin/env python

# commit_data.py

import os
import sys
import json
import urllib3
from static_config import environment_variables, write_vars
dynamic_config = json.load(open('dynamic_config.json','r'))

def commit_data():
    loaded = []
    for _file in os.popen('ls cache*').read().split('\n'):
        if os.path.isfile(_file):
            with open(_file) as f:
                for line in f.readlines():
                    loaded.append(json.loads(line))
                only_vals_string = _file.replace('cache-', '')
                implicit_values_dict = dict(zip(
                    environment_variables, only_vals_string.split('_-_')
                ))
                loaded[-1].update(implicit_values_dict)
    print(loaded)
    http = urllib3.PoolManager(maxsize=len(loaded))
    for loaded_item in loaded:
        r = http.request(
            'GET',
            dynamic_config['next_url'],
            fields=loaded_item
        )
        print(r)



if __name__ == "__main__":
    commit_data()
