import json
import requests


class PacientDetailService:

    def __init__(self):
        pass

    def lambda_handler(self, event, context):
        x = requests.get('https://w3schools.com/python/demopage.htm')
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": "hello from CI GIT!" + x.text,
                }
            ),
        }
