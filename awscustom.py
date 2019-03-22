import boto3

client = boto3.client('sns')    

def send_sns(sns_topic_arn=None,sns_subject=None,sns_message=None,sns_source=None):

    full_subject = sns_subject + " : " + sns_source

    full_message = sns_message + " : " + sns_source

    print(client.publish(TopicArn=sns_topic_arn,Subject=full_subject,Message=full_message))
