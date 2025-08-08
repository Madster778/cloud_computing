# Python and AWS S3 with Boto3 – Practical Notes

These notes summarise Boto3 and S3 implementation tasks: listing objects, reading objects, loading data to pandas, and writing data back to S3, plus a small ETL example.

---

## Prerequisites

- AWS credentials configured locally using the shared credentials files

```
~/.aws/credentials
~/.aws/config
```

- Region set to `eu-central-1`
- Python environment with the following libraries:

```
boto3
pandas
```

- **Never** hard-code access keys in scripts.

---

## Clients and Resources in Boto3

Boto3 offers two S3 interfaces:

| Feature        | Client                      | Resource                                     |
| -------------- | --------------------------- | -------------------------------------------- |
| Level          | Low-level API               | High-level, Pythonic                         |
| Method mapping | Direct to AWS REST API      | Abstracted methods                           |
| Example        | `s3_client.get_object(...)` | `s3_resource.Bucket('bucket').objects.all()` |

```python
import boto3

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
```

---

## Listing Buckets and Objects

### List buckets (resource):

```python
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
```

### List objects in a bucket (resource):

```python
bucket = s3.Bucket('data-eng-resources')
for obj in bucket.objects.all():
    print(obj.key)
```

### List objects in a bucket (client):

```python
response = s3_client.list_objects_v2(Bucket='data-eng-resources')
for obj in response.get('Contents', []):
    print(obj['Key'])
```

**Difference summary:**  
Client returns dictionaries that you parse. Resource returns Python objects like `ObjectSummary` with attributes such as `.key`, `.size`, `.last_modified`.

---

## Reading an Object with `get_object`

`get_object` is available on the client.  
Read the object body, decode text, then use it as needed:

```python
response = s3_client.get_object(
    Bucket='data-eng-resources',
    Key='python/happiness-2019.csv'
)
text = response['Body'].read().decode('utf-8')
print(text[:500])
```

---

## Loading a CSV from S3 into Pandas

```python
import pandas as pd
from io import StringIO

response = s3_client.get_object(
    Bucket='data-eng-resources',
    Key='python/happiness-2019.csv'
)
csv_text = response['Body'].read().decode('utf-8')

df = pd.read_csv(StringIO(csv_text))
print(df.head())
```

---

## Writing Objects to S3

### Upload a JSON object to your folder:

```python
import json

data = {
    "name": "Mohammed Mahdi Alom",
    "role": "Data Consultant Trainee",
    "interest": "Data Analytics",
    "learning": "AWS",
    "fact": "I am left handed"
}

s3_client.put_object(
    Bucket='data-eng-resources',
    Key='Mahdi/mahdi-info.json',
    Body=json.dumps(data),
    ContentType='application/json'
)
```

---

### Upload a Pandas DataFrame directly to S3:

```python
from io import StringIO

# Load DataFrame from CSV in S3
response = s3_client.get_object(
    Bucket='data-eng-resources',
    Key='python/happiness-2019.csv'
)
csv_text = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv_text))

# Convert DataFrame to CSV in memory
buffer = StringIO()
df.to_csv(buffer, index=False)

# Upload to S3
s3_client.put_object(
    Bucket='data-eng-resources',
    Key='Mahdi/happiness-2019-copy.csv',
    Body=buffer.getvalue(),
    ContentType='text/csv'
)
```

---

## Mini ETL Example: Fish Market Data

Goal: average numeric columns by species and upload to your folder.

```python
response = s3_client.get_object(
    Bucket='data-eng-resources',
    Key='python/fish-market.csv'
)
text = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(text))

# Transformation
df_out = df.groupby('Species').mean(numeric_only=True).reset_index()

# Upload result
buf = StringIO()
df_out.to_csv(buf, index=False)

s3_client.put_object(
    Bucket='data-eng-resources',
    Key='Mahdi/fish-transformed.csv',
    Body=buf.getvalue(),
    ContentType='text/csv'
)
```

---

## Tips & Checks

- Always verify bucket and key names before running code.
- Prefer `StringIO` for in-memory read/write with Pandas to avoid local files.
- Use `print()` sparingly for debugging (e.g., printing keys or DataFrame heads).
- Never commit AWS credentials — rely on `~/.aws/credentials` or environment variables.
