#!/usr/bin/env python2
#http://stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json
#kudos to jdi and R K
#One option for the posting of data to the database
import json
import urllib2

class PostData(object):
    def __init__(self):
        data = dict(
            Location = None
            TypeOfSensor = None
            SensorId = None
            TestType = None
            SensorOwner = None
            SensorValue = None
            ReportedTriggerValue = None
            ReportedThresholdValue = None
            ReportedNormalValue = None
            SensorUnits = None
        )
    def post(self):
        req = urllib2.Request('http://localhost:8000/upload.php')
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(data))
        return response
