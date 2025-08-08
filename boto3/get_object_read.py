import boto3

# Step 1: Create a client
s3_client = boto3.client('s3')

# Step 2: Fetch the CSV file
response = s3_client.get_object(
    Bucket='data-eng-resources',
    Key='python/happiness-2019.csv'
)

# Step 3: Read and decode the content
body = response['Body'].read()
text = body.decode('utf-8')

# Step 4: Preview it
print(text)
