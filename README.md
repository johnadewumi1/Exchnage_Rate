# Exchnage_Rate
This projrct is to get daily exchange rate and store the output in an s3 bucket and also send email to the security team for any failed on rate or upload.



#ARCHITECTURAL DIAGRAM

![image](https://github.com/johnadewumi1/Exchnage_Rate/blob/main/Image/archi.png)

# Project Statement
I am starting an Exchange Company, and I want to get the rate at which exchange rate fluctuates from USD to (insert your currency of choice) 
I want to get and export of the exchange rate as a JSON output every hour into an S3 bucket. I also want to be notified once this is completed. 

##SOLUTION

1. log into, ([aws console](https://s3.console.aws.amazon.com)) and create EC2 instanceof your desired, ensure you can SSH into it. see the cfn tamplate for ec2.

2. Cteate an SNS to send email to your security team when their is failure. Check Cfn tamplate for Sns resources.

3. Create S3 bucket that for you to out the json file output from the EC2. see how to create s3 ([s3 bucket documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)). A cloud formation template above named s3.yaml was used to create one for this project.

4. Create an ***IAM Role*** and attach a ***IAM Policy*** that enable your **ec2** to put object and publish sns notification to the right resources. Policy already in the repository, check **iam-policy.json**. Copy the policy and paste after creating your role.

5. Replace your BuckeNmane & TopicArn in the code for accurate deployment.

6. SSH into the EC2 with any tools you are familiar with, Once you are in, you create a virtual environment using the command ```python3 -m venv venv``` after executing this command, activate the virtual environment with the command ```source venv/bin/activate``` This activates your virtual environment

![image](https://github.com/johnadewumi1/Exchnage_Rate/blob/main/Image/ssh.png)

7. Install the various python package libraries needed for the project to run in the EC2 instance.
``` 
  pip3 install pandas
  pip3 install boto3 
  pip3 install jsons 
  pip3 install requests
  pip3 install forex-python
  pip3 install python-dotenv
```

8. Creating directories and files for thr scripts to run
 * Create Directory called xchage
 * In xchange directory, create 2 directories called ```data``` and ```scripts```
 * Go inside scripts and create 2 files called
   * exchange_rate.py ( this will contain the python script to run the exchage rate)
   * runscripts.sh ( this will be use to run the python script above)
 * Create a cron job in the home directory **crontab -e** that will be used to run the job daily  or hourly depend on how ypu want information.(learn how to create cron job). Check the ***crontab -e.sh*** for script you might want to input.

 8. create a new python script(check ***xchage_scrip.py*** for the code) that would take in various exchange rates of the world's currency and output it. provide a name for this script. and upload it to the EC2 instance in the exchange_rate.py by ``` vim exchange_rate.py``` paste the code and save by using this on your windows computer.
    ```
        Esc
        :wq
    ```

9. Create .env file looks like this. Make sure you replace the values with the ones you got from the previous step.
```
    AWS_ACCESS_KEY_ID=your-access-key-id
    AWS_SECRET_ACCESS_KEY=your-secret-access-key
```

9. The bash script named ***runscripts.sh* it's atteched in the repository, this will trigger the python scripts (exchange_rate.py) and also the SNS

10. The ***crontab -e*** enables the code to run at a regulat schedule prefered for the purpose of your project. Check ***crontab -e.sh***, I created for 5mins and hourly schedule.

**When the cron job triggers on schedule, you receive an SNS email notification will be sent**
![image](https://github.com/johnadewumi1/Exchnage_Rate/blob/main/Image/email.png)
