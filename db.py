import boto3
import os
from decimal import *
from boto3.dynamodb.conditions import Key, Attr

# AWS
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

# User and Login
def getUsrInfo(usr: str):
    return usrs.query(KeyConditionExpression=Key('usr').eq(usr))['Items'][0]

def getSessInfo(sess: str):
    return sesss.query(KeyConditionExpression=Key('sess').eq(sess))['Items'][0]

def createRawUsr(usr: str, name: str, hash: str, created: float, lvl: int, lastLvlChange: str):
    usrs.put_item(Item={
        'usr': usr,
        'name': name,
        'hash': hash,
        'created': Decimal(created),
        'lvl': lvl,
        'lastLvlChange': lastLvlChange
    })

def grant(giver: str, getter: str, lvl: int):
    usrs.update_item(
        Key={
            'usr': getter,
            'name': getUsrInfo(getter)['name']
        },
        UpdateExpression="set lvl = :l, lastLvlChange = :c",
        ExpressionAttributeValues={
            ':l': lvl,
            ':c': giver
        }
    )

def createRawSess(sess: str, usr: str, ip: str, time: float):
    sesss.put_item(Item={
        'sess': sess,
        'usr': usr,
        'ip': ip,
        'time': Decimal(time)
    })

def rmSess(sess: str):
    sesss.delete_item(
        Key={
            'sess': sess
        }
    )

# Match Scouting
def getMatchInfo(id : str):
    return match.query(KeyConditionExpression=Key('id').eq(id))['Items'][0]

def matchAdd(id: str, team: int, habStart: int, ac: int, ah: int, tha: int, thd: int, thl: int, thm: int, thh: int, tca: int, tcd: int, tcl: int, tcm: int, tch: int, habEnd: int, ct: float, c: str):
    match.put_item(Item={
        'id': id,
        'team': team,
        'auto': {
            'habStart': habStart,
            'cargo': ac,
            'hatch': ah
        },
        'teleop': {
            'hatch': {
                'aq': tha,
                'drop': thd,
                'low': thl,
                'mid': thm,
                'high': thh
            },
            'cargo': {
                'aq': tca,
                'drop': tcd,
                'low': tcl,
                'mid': tcm,
                'high': tch
            }
        },
        'end': {
            'habEnd': habEnd,
            'climbTime': Decimal(ct)
        },
        'comments': c
    })