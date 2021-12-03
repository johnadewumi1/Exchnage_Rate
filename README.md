# Exchnage_Rate
This projrct is to get daily exchange rate and store the output in an s3 bucket



#ARCHITECTURAL DIAGRAM

![image](https://github.com/johnadewumi1/Exchnage_Rate/blob/main/Image/archi.png)

# Project Statement
I am starting an Exchange Company, and I want to get the rate at which exchange rate fluctuates from USD to (insert your currency of choice) 
I want to get and export of the exchange rate as a JSON output every hour into an S3 bucket. I also want to be notified once this is completed. 

##SOLUTION

1. log into, ([aws console](https://s3.console.aws.amazon.com)) and create EC2 instanceof your desired, ensure you can SSH into it. see the cfn tamplate for ec2.
2. Create S3 bucket that for you to out the json file output from the EC2. see how to create s3 ([s3 bucket documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)). A cloud formation template above s3.yaml was usede to create one for this project.
3. Create an ***IAM Role*** and attach a ***IAM Policy*** that enable your **ec2** to put object and publish sns notification to the right resources. Policy already in the repository, check **iam-policy.json**. Copy the policy and paste after creating your role.
4. Replace your BuckeNmane & TopicArn in the code for accurate deployment.




