#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS=/home/preeth_god/pipelines-demo-309822-91076e886af7.json
if [ $# != 2 ]
	then
	echo "Invalid args supplied"
	exit 12
fi

job_name=$1
dataset_name=$2
#source_database_name=$3

bq mk \
	--transfer_config \
	--project_id=pipelines-demo-309822 \
	--target_dataset=$dataset_name \
	--display_name=$job_name \
	--params='{"bucket": "my_bucket123465", "database_type": "Teradata",
"database_name":"customers", "table_name_patterns": ".*",
if [ $# != 2 ]
	then
	echo "Invalid number of args supplied"
	exit(12)
else
	echo "Valid arguments"
fi
"agent_service_account":"tdtransfer@pipelines-demo-309822.iam.gserviceaccount.com", "schema_file_path":
"gs://my_bucket123465/td_to_bd_schema.json"}' \
	--data_source=on_premises

if [ $? == 0 ]
	then
	echo "Completed sucessfully"
else
	echo "failed"
	exit 12
fi