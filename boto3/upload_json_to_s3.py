import boto3
import json

# Prepare data
data = {
    "name": "Mohammed Mahdi Alom",
    "role": "Data Consultant Trainee",
    "interest": "Data Analytics",
    "learning": "AWS",
    "fact": "I'm left handed"
}

# Convert to JSON
json_data = json.dumps(data)

# Upload to S3
s3_client = boto3.client('s3')
s3_client.put_object(
    Bucket='data-eng-resources',
    Key='Mahdi/mahdi-info.json',
    Body=json_data,
    ContentType='application/json'
)

print("JSON uploaded to Mahdi/mahdi-info.json")
