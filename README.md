# Exchnage_Rate
This projrct is to get daily exchange rate and store the output in an s3 bucket



#ARCHITECTURAL DIAGRAM

![image](https://github.com/johnadewumi1/Exchnage_Rate/blob/main/Image/archi.png)

# Project Statement
I am starting an Exchange Company, and I want to get the rate at which exchange rate fluctuates from USD to (insert your currency of choice) 
I want to get and export of the exchange rate as a JSON output every hour into an S3 bucket. I also want to be notified once this is completed. 

##SOLUTION

1. log into, (aws console)[https://s3.console.aws.amazon.com]
2. In Define Pattern, choose Event pattern.
3. In Event Matching pattern, choose Custom pattern.
4. In the Event pattern preview pane, copy and paste the following example event pattern: use Event_pattern.json template




