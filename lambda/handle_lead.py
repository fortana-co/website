from typing import List
import os
from urllib.parse import parse_qs

import boto3
import json


def get_ses_client():
    return boto3.client(
        'ses',
        aws_access_key_id=os.getenv('CUSTOM_AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('CUSTOM_AWS_SECRET_KEY'),
        region_name='us-west-2',
    )


def send_email(
    to: List[str],
    subject: str,
    body: str,
    source: str = 'Fortana <donotreply@brigada.mx>',
    reply_to: List[str] = None,
    **kwargs,
):
    return get_ses_client().send_email(
        Source=source,
        Destination={
            'ToAddresses': to,
        },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'UTF-8',
            },
            'Body': {
                'Html': {
                    'Data': body,
                    'Charset': 'UTF-8',
                },
            },
        },
        ReplyToAddresses=reply_to or [],
    )


def respond(body, status_code=200, headers=None):
    return {
        'statusCode': status_code,
        'body': json.dumps(body),
        'headers': headers or {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
    }


def lambda_handler(event, context):
    method = event['httpMethod']
    if method != 'POST':
        return respond({'error': 'method not allowed'}, 400)

    body = parse_qs(event['body'])  # Content-Type: application/x-www-form-urlencoded
    name, org, email, project = body['name'][0], body['org'][0], body['email'][0], body['project'][0]

    send_email(['kyle@fortana.co'], f'New Lead - {name}',
               f"""Someone filled out Fortana's lead form with the following information:<br><br>
               <b>Name</b>: {name}<br>
               <b>Organization</b>: {org}<br>
               <b>Email</b>: {email}<br>
               <b>Project</b>: {project}""")
    return respond({})
