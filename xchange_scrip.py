
import json
import boto3
import requests
import os
import forex_python
from dotenv import load_dotenv

load_dotenv()
from datetime import datetime
now_latest = datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

from forex_python.converter import CurrencyRates
cu = CurrencyRates ()
rate = cu.get_rates('USD')
rate_json= now_latest + '.json'
#print(rate)

#serialized json
json_file = json.dumps(rate, indent = 4)

#define s3 properties to upload
def upload_to_s3(rate_json):
    file_name = rate_json
    bucket_name = 'exchange-rate-bucket1'
    s3_client = boto3.client(
    's3', 
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)
    response = s3_client.upload_file(file_name,bucket_name,file_name)




#write to file
with open(rate_json, 'w') as outfile:
    outfile.write(json_file)
    upload_to_s3(rate_json)


# send SNS message with warning and bucket policy
sns = boto3.client("sns", region_name='us-west-1')
bucket_name = 'exchange-rate-bucket1'
subject =  rate_json + " has been uploaded"
message = 'Hello, the latest exchange rate has been uploaded in the' + bucket_name + 'kindly update the customer data for the new market rate'


response = sns.publish(

    TopicArn = 'arn:aws:sns:us-east-1:672432851135:ExchangeRate',
    Subject = subject,
    Message = message
)