import boto3
import os
from boto3.dynamodb.conditions import Key, Attr

aws = boto3.Session(
    aws_access_key_id=os.environ['AWS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_KEY_SECRET'],
    region_name='us-east-1'
)
db = aws.resource('dynamodb')

usrs = db.Table('6479-tracker-users')
sesss = db.Table('6479-tracker-sess')
match = db.Table('6479-tracker-match')
pit = db.Table('6479-tracker-pit')

def getUsrInfo(usr: str):
    return usrs.query(KeyConditionExpression=Key('usr').eq(usr))['Items'][0]

def createRawUsr(usr: str, name: str, hash: str, created: float, lvl: int, lastLvlChange: str):
    usrs.put_item(Item={
        'usr': usr,
        'name': name,
        'hash': hash,
        'created': created,
        'lvl': lvl,
        'lastLvlChange': lastLvlChange
    })
def createRawSess(sess: str, usr: str, ip: str, time: float):
    sesss.put_item(Item={
        'sess': sess,
        'usr': usr,
        'ip': ip,
        'time': time
    })