import json
import requests
import boto3
import forex_python
from datetime import datetime
now_latest=datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

from forex_python.converter import CurrencyRates
cu = CurrencyRates ()
rate = cu.get_rates('USD')
rate_json= now_latest + '.json'
#print(rate)

#serialized json
json_file = json.dumps(rate, indent = 5)

#write to file
with open(rate_json, 'w') as outfile:
    outfile.write(json_file)

sns_client = boto3.client('sns')
s3_client = boto3.client('s3', region_name= 'us-east-1')
s3_name = now_latest + '.json'

with open (rate_json, 'rb') as f:
    s3.upload_file(f, 'exchange-rate-bucket1', s3_name)
#print(rate_json)

sns_client.publish(TargetArn = 'arn:aws:sns:us-east-1:672432851135:ExchangeRate', Message = 
'Hello Team \n below is the file that is being drop in your s3 bucket for latest exchnage rate' + rate_json)
#print(rate_json)

