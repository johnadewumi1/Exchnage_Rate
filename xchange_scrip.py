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





import json
import boto3
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
json_file = json.dumps(rate, indent = 5)

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
    upload_to_s3(json_file)


# AWS_ACCESS_KEY_ID=AKIAZZEA7BC7QHVCAI23
# AWS_SECRET_ACCESS_KEY=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




# import json
# import requests
# import boto3
# import forex_python
# from datetime import datetime
# now_latest=datetime.today().strftime('%Y_%m_%d_%H_%M_%S')

# from forex_python.converter import CurrencyRates
# cu = CurrencyRates ()
# rate = cu.get_rates('USD')
# rate_json= now_latest + '.json'
# #print(rate)

# #serialized json
# json_file = json.dumps(rate, indent = 5)

# #write to file
# with open(rate_json, 'w') as outfile:
#     outfile.write(json_file)
