import json
import boto3
import datetime

def insert_item(event, context):

    dynamodb = boto3.resource('dynamodb')


    table = dynamodb.Table('Yortzeit')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
    print(table.creation_date_time)
# import requests
#print("hello World!")


    table.put_item(
        Item={
            'y_id':datetime.datetime.utcnow().isoformat(),
            'name': 'ortal',
            'last_name': 'Doe',
            'email': 'jhv@hksdbvb.com',
        }
    )

     
    return {
        "statusCode": 200,
        "body": json.dumps({
      "message":"hello world"
        }),
    }
   
    
    