import json
import urllib.parse
import boto3
import os

print('Loading function...')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    src_bucket = 's3-test-202009'
    dst_bucket = 's3-testdst-202009'
    filename = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print(filename)
    
    try:
        response = s3.copy_object(Bucket=dst_bucket, Key=filename, CopySource={'Bucket': src_bucket, 'Key': filename})
        return True
    except Exception as e:
        print(e)
