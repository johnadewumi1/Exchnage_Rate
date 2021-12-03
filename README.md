# Exchnage_Rate
This projrct is to get daily exchange rate and store the output in an s3 bucket



#ARCHITECTURAL DIAGRAM

![image](https://github.com/johnadewumi1/Exchnage_Rate/blob/main/Image/archi.png)

# Project Statement
I am starting an Exchange Company, and I want to get the rate at which exchange rate fluctuates from USD to (insert your currency of choice) 
I want to get and export of the exchange rate as a JSON output every hour into an S3 bucket. I also want to be notified once this is completed. 

##SOLUTION

1. log into, ([aws console](https://s3.console.aws.amazon.com)) and create EC2 instanceof your desired, ensure you can SSH into it. see the cfn tamplate for ec2.
2. Create S3 bucket that for you to out the json file output from the EC2. see how to create s3 ([s3 bucket documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)). A cloud formation template above named s3.yaml was used to create one for this project.
3. Create an ***IAM Role*** and attach a ***IAM Policy*** that enable your **ec2** to put object and publish sns notification to the right resources. Policy already in the repository, check **iam-policy.json**. Copy the policy and paste after creating your role.
4. Replace your BuckeNmane & TopicArn in the code for accurate deployment.
5. SSH into the EC2 with any tools you are familiar with, Once you are in, you create a virtual environment using the command ```python3 -m venv venv``` after executing this command, activate the virtual environment with the command ```source venv/bin/activate``` This activates your virtual environment

![image](https://github.com/johnadewumi1/Exchnage_Rate/blob/main/Image/ssh.png)

6. Create directories and folders
 * Create Directory called xchage
 * in xchange directory, create 2 directories called ```data``` and ```scripts```
 * go inside scripts and create 2 files called
   * exchange_rate.py ( this will contain the python script to run the exchage rate)
   * runscripts.sh ( this will be use to run the python script above)





