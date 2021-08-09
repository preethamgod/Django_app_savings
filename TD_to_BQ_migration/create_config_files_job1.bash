#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS=/home/preethamgod/pipelines-demo-309822-91076e886af7.json
script_var=$0
migration_path=/home/preethgod/migration
java -cp /home/preethgod/migration/tdgssconfig.jar:/home/preethgod/migration/terajdbc4.jar:/home/preethgod/migration/mirroring-agent.jar com.google.cloud.bigquery.dms.Agent --initialize << EOF
yes
$migration_path/temp_$script_var
/home/preethgod/migration/staging_area/
192.168.207.128
1025
yes
/home/preethgod/migration/config/cds.txt
projects/247710760794/locations/us/transferConfigs/61e0ff3b-0000-2949-899e-883d24f9f28c
$migration_path/config/config_$script_var.json
EOF
if [ $? == 0 ]
	then
	echo "Completed sucessfully"
else
	echo "failed"
	exit 12
fi
	



