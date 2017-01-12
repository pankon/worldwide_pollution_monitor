#!/usr/bin/env python2
#http://stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json
#kudos to jdi and R K
#One option for the posting of data to the database
import json
# import urllib2

class PostData(object):
    def __init__(self):
        data = dict(
            Location = None,
            TypeOfSensor = None,
            SensorId = None,
            TestType = None,
            SensorOwner = None,
            SensorValue = None,
            ReportedTriggerValue = None,
            ReportedThresholdValue = None,
            ReportedNormalValue = None,
            SensorUnits = None
        )
    # def post(self):
    #     req = urllib2.Request('http://localhost:8000/upload.php')
    #     req.add_header('Content-Type', 'application/json')
    #     response = urllib2.urlopen(req, json.dumps(data))
    #     return response

def gen_sample_query():
    post_data = PostData()
    post_data.data = dict(
        Location = "'[Latitude, Longitude]'",
        TypeOfSensor = "'CompanyName-Phosphorus model 001A'",
        SensorId = "'IdString'",
        TestType = "'Phosphorus'",
        SensorOwner = "'Ploni'",
        SensorValue = "'1.23545434'",
        ReportedTriggerValue = "'1.4'",
        ReportedThresholdValue = "'1.3'",
        ReportedNormalValue = "'1.24'",
        SensorUnits = "'ppm'"
    )
    sConnect = 'http://localhost:8000/upload.php?'
    lItems = ['='.join(item) for item in post_data.data.items()]
    sConnect += '&'.join(lItems)
    print(sConnect)

if __name__ == '__main__':
    gen_sample_query()
