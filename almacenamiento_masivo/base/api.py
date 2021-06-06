import boto3
import json


def get_var_char_values(d):
    return [obj['VarCharValue'] for obj in d['Data']]


def run_api():
    aws_access_key_id = 'AKIA4UBERADCUIK37A74'
    aws_secret_access_key = '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'

    athena = boto3.client(
        'athena',
        region_name='us-east-1',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    athena_job_query = athena.start_query_execution(
        QueryString='SELECT * FROM listing_data limit 5;',
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

    print(json.dumps(result, indent=2))
    """for table in response['ResultSet']['Rows']:
        for row in table['Data']:
            print(row)
        print()"""
