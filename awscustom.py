import boto3

client = boto3.client('sns',region_name='ap-southeast-2')    

def send_sns(sns_topic_arn="",sns_subject="",sns_message="",sns_source=""):

    full_subject = sns_subject + " : " + sns_source

    full_message = sns_message + " : " + sns_source

    print(client.publish(TopicArn=sns_topic_arn,Subject=full_subject,Message=full_message))
