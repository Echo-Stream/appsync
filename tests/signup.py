#!/usr/bin/env python3.8
from boto3 import client

client = client("cognito-idp")

response = client.sign_up(
    ClientId="foo",
    Username="yo@momma.com",
    Password="",
    UserAttributes=[
        {
            "Name": "given_name",
            "Value": "Joe"
        },
        {
            "Name": "family_name",
            "Value": "Wortman"
        }
    ]
)
