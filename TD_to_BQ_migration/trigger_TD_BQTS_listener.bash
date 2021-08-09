#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS=/home/preethamgod/pipelines-demo-309822-91076e886af7.json

if [ $# != 1 ]
	then
	echo "Invalid args supplied"
	exit 12
fi
config_file=$1

java -cp /home/preethgod/migration/tdgssconfig.jar:/home/preethgod/migration/terajdbc4.jar:/home/preethgod/migration/mirroring-agent.jar com.google.cloud.bigquery.dms.Agent --configuration-file=$config_file
if [ $? == 0 ]
	then
	echo "Completed sucessfully"
else
	echo "failed"
	exit 12
fi