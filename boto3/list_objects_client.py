import boto3

s3_client = boto3.client('s3')
response = s3_client.list_objects_v2(Bucket='data-eng-resources')

for obj in response.get('Contents', []):
    print(obj['Key'])
