import json
import boto3
import os
# import requests

if os.environ["AWS_SAM_LOCAL"]:
    dynamodb_client = boto3.client('dynamodb', endpoint_url="http://dynamodb-local:8000")
else:
    dynamodb_client = boto3.client('dynamodb')


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    dynamodb_client.put_item(TableName='dynamodb-table2', Item={'id': {'S': '11'}, 'date': {'N': "1"}, 'score': {'N': "100"}})
    dynamodb_client.put_item(TableName='dynamodb-table2', Item={'id': {'S': '21'}, 'date': {'N': "2"}, 'score2': {'N': "200"}})

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"hello world23{os.environ['TABLE_NAME']}",
            # "location": ip.text.replace("\n", "")
        }),
    }
