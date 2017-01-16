<?php
    $vars = array(
        'Location',
        'TypeOfSensor',
        'SensorId',
        'TestType',
        'SensorOwner',
        'SensorValue',
        'ReportedTriggerValue',
        'ReportedThresholdValue',
        'ReportedNormalValue',
        'SensorUnits',
    );
    $input = '';
    foreach($vars as &$value) {
        $input=$input.$value.':'.$_GET[$value].' ';
    }
    $command = "python point_commit.py $input";
    echo $input;
    $handle = popen($command, 'r');
    $output = fread($handle, 2096);
    echo $output;
    fclose($handle);
?>
