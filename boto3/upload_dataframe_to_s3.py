import boto3
import pandas as pd
from io import StringIO

# Load original CSV from S3
s3_client = boto3.client('s3')
response = s3_client.get_object(
    Bucket='data-eng-resources',
    Key='python/happiness-2019.csv'
)

body = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(body))

# Convert DataFrame to in-memory CSV
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

# Upload to your folder in S3
s3_client.put_object(
    Bucket='data-eng-resources',
    Key='Mahdi/happiness-2019-copy.csv',
    Body=csv_buffer.getvalue(),
    ContentType='text/csv'
)

print("DataFrame uploaded to Mahdi/happiness-2019-copy.csv")
