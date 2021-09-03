#!/usr/bin/env python3.8
from boto3 import client
from pprint import pprint

c = client("kms")

res = c.list_grants(
    KeyId="arn:aws:kms:us-east-1:066817783078:key/cd0df61e-9a9e-46df-8b21-fc40d4468f53"
)

pprint(res)
