import json
import boto3

def lambda_handler(event, context):
    # Example: create EC2 client
    ec2_client = boto3.client('ec2')

    # Fetch list of EC2 instances
    response = ec2_client.describe_instances()

    # Extract instance IDs for demonstration
    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    # Build Lambda JSON response
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': 'EC2 instances fetched successfully!',
            'instances': instance_ids
        })
    }

