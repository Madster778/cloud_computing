import boto3
import pandas as pd
from io import StringIO

# Step 1: Connect to S3 and get the original fish data
s3_client = boto3.client('s3')
response = s3_client.get_object(
    Bucket='data-eng-resources',
    Key='python/fish-market.csv'
)

# Step 2: Load into DataFrame
csv_data = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_data))

# Step 3: Transformation - average numeric columns by species
df_transformed = df.groupby('Species').mean(numeric_only=True).reset_index()

# Step 4: Prepare in-memory CSV
csv_buffer = StringIO()
df_transformed.to_csv(csv_buffer, index=False)

# Step 5: Upload to your Mahdi folder in S3
s3_client.put_object(
    Bucket='data-eng-resources',
    Key='Mahdi/fish-transformed.csv',
    Body=csv_buffer.getvalue(),
    ContentType='text/csv'
)

print("fish-transformed.csv uploaded to Mahdi/ in data-eng-resources.")
