import boto3
import json
import os
from django.conf import settings


def get_var_char_values(d):
    return [obj['VarCharValue'] for obj in d['Data']]


def run_api(query_string):
    aws_access_key_id = settings.AWS_ACCESS_KEY_ID
    aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY

    athena = boto3.client(
        'athena',
        region_name=settings.REGION,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    athena_job_query = athena.start_query_execution(
        QueryString=query_string,
        QueryExecutionContext={
            'Database': 'grupo3_db'
        },
        ResultConfiguration={
            'OutputLocation': 's3://aypmd-grupo3/athena/'
        }
    )

    query_execution_id = athena_job_query['QueryExecutionId']

    athena_job_status_query = athena.get_query_execution(QueryExecutionId=query_execution_id)
    while athena_job_status_query['QueryExecution']['Status']['State'] != 'SUCCEEDED':
        athena_job_status_query = athena.get_query_execution(QueryExecutionId=query_execution_id)
        print(athena_job_status_query['QueryExecution']['Status']['State'])

    args = {
        'QueryExecutionId': query_execution_id,
        'MaxResults': 300,
        }
    response = athena.get_query_results(**args)

    header, *rows = response['ResultSet']['Rows']
    header = get_var_char_values(header)
    result = [dict(zip(header, get_var_char_values(row))) for row in rows]
    json_data = json.dumps(result, indent=2)
    return json_data
