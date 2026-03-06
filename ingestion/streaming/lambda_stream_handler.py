import json
import boto3
import datetime

s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

def handler(event, context):
    table = dynamodb.Table("custom_app_stream")

    for record in event.get("records", []):
        table.put_item(Item=record)

        s3.put_object(
            Bucket="enterprise-raw-zone",
            Key=f"stream/{datetime.date.today()}/{record['id']}.json",
            Body=json.dumps(record)
        )

    return {"statusCode": 200}