<?php
    $Location = $_GET['Location']
    $TypeOfSensor = $_GET['TypeOfSensor']
    $SensorId = $_GET['SensorId']
    $TestType = $_GET['TestType']
    $SensorOwner = $_GET['SensorOwner']
    $SensorValue = $_GET['SensorValue']
    $ReportedTriggerValue = $_GET['ReportedTriggerValue']
    $ReportedThresholdValue = $_GET['ReportedThresholdValue']
    $ReportedNormalValue = $_GET['ReportedNormalValue']
    $SensorUnits = $_GET['SensorUnits']
    $input = '{Location=$Location, TypeOfSensor=$TypeOfSensor, SensorId=$SensorId, SensorOwner=$SensorOwner, SensorValue=$SensorValue, ReportedTriggerValue=$ReportedTriggerValue, ReportedThresholdValue=$ReportedThresholdValue, ReportedNormalValue=$ReportedNormalValue, SensorUnits=$SensorUnits]'
    $command = "python process_input.py $input > output.txt";
    popen($command, 'r');
?>
