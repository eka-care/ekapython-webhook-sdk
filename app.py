import json
from webhook_consumer import (WebhookConsumer)

def submit(event):
    try:
        escaped_json = event.get('body')
        unescaped_json = escaped_json.encode('utf-8').decode('unicode_escape')
        body = json.loads(unescaped_json)

        webhook_consumer = WebhookConsumer(body)
        webhook_data = webhook_consumer.get_data()
        return {
            'statusCode': 200,
            'body': json.dumps(webhook_data)
        }
    except Exception as e:
        print("Exception handling webhook data:", e)
        return {
            'statusCode': 500,
            'body': 'Internal Error'
        }

def lambda_handler(event, context):
    path = event.get('rawPath') or event.get('path')
    method = event.get('requestContext', {}).get('http', {}).get('method') or event.get('httpMethod')

    print(f"path : {path}")
    print(f"method : {method}")
    print(f"event : {event}")

    # TODO: Add better Route handling; flask ?
    if method == 'POST' and path == '/webhook':
        return submit(event)
    else:
        return {
            'statusCode': 404,
            'body': 'Not Found'
        }
