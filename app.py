from webhook_consumer import WebhookConsumer


def submit(event):
    import json
    body = json.loads(event.get('body') or '{}')
    try:
        webhook_consumer = WebhookConsumer()
        webhook_consumer.print_data(body)
        return {
            'statusCode': 200,
            'body': json.dumps({'received': body})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': 'Internal Error'
        }

def lambda_handler(event, context):
    path = event.get('rawPath') or event.get('path')
    method = event.get('requestContext', {}).get('http', {}).get('method') or event.get('httpMethod')


    if method == 'POST' and path == '/webhook':
        return submit(event)
    else:
        return {
            'statusCode': 404,
            'body': 'Not Found'
        }
