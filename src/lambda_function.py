import json
import requests



def lambda_handler(event, context):
    x = requests.get('https://w3schools.com/python/demopage.htm')
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello from CI GIT pipline dev!" + x.text,
            }
        ),
    }

def lambda_handler_duplication(event, context):
    x = requests.get('https://w3schools.com/python/demopage.htm')
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello from CI GIT pipline dev!" + x.text,
            }
        ),
    }