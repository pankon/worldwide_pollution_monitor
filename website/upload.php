<?php
    $Location = 'Location'.':'.$_GET['Location'];
    $TypeOfSensor = 'TypeOfSensor'.':'.$_GET['TypeOfSensor'];
    $SensorId = 'SensorId'.':'.$_GET['SensorId'];
    $TestType = 'TestType'.':'.$_GET['TestType'];
    $SensorOwner = 'SensorOwner'.':'.$_GET['SensorOwner'];
    $SensorValue = 'SensorValue'.':'.$_GET['SensorValue'];
    $ReportedTriggerValue = 'ReportedTriggerValue'.':'.$_GET['ReportedTriggerValue'];
    $ReportedThresholdValue = 'ReportedThresholdValue'.':'.$_GET['ReportedThresholdValue'];
    $ReportedNormalValue = 'ReportedNormalValue'.':'.$_GET['ReportedNormalValue'];
    $SensorUnits = 'SensorUnits'.':'.$_GET['SensorUnits'];
    $input = $Location." ".$TypeOfSensor." ".$SensorId." ".$SensorOwner." ".$SensorValue." ".$ReportedTriggerValue." ".$ReportedThresholdValue." ".$ReportedNormalValue." ".$SensorUnits;
    $command = "python process_input.py $input >> cache";
    //$input > output.txt";
    echo $input;
    $handle = popen($command, 'r');
    $output = fread($handle, 2096);
    echo $output;
    //echo $input;
    fclose($handle);
?>
