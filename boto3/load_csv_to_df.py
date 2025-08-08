import boto3
import pandas as pd
from io import StringIO

# Step 1: Connect to S3 and get the CSV file
s3_client = boto3.client('s3')
response = s3_client.get_object(
    Bucket='data-eng-resources',
    Key='python/happiness-2019.csv'
)

# Step 2: Decode the binary response
body = response['Body'].read()
text = body.decode('utf-8')

# Step 3: Load the text into a Pandas DataFrame
csv_buffer = StringIO(text)
df = pd.read_csv(csv_buffer)

# Step 4: Preview the DataFrame
print(df)
print(df.columns)
