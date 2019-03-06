import boto3
import os

aws = boto3.Session(
    aws_access_key_id=os.environ['AWS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_KEY_SECRET'],
    region_name='us-east-1'
)
db = aws.resource('dynamodb')

usrs = db.Table('6479-tracker-users')
sess = db.Table('6479-tracker-sess')
match = db.Table('6479-tracker-match')
pit = db.Table('6479-tracker-pit')

def getPwdHash(usr):
    # TODO: write code
    # Below is an Argon2 hash of "password"
    return "$argon2i$v=19$m=512,t=2,p=2$aI2R0hpDyLm3ltLa+1/rvQ$LqPKjd6n8yniKtAithoR7A"