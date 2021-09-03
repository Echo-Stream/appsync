#!/usr/bin/env python3.8
from appsync import callAppsync
from time import sleep
from json import dumps


mutation = """
    mutation putKey($tenant: String!, $key: KmsKeyInput!) {
        PutKmsKey(key: $key, tenant: $tenant){
            name,
            description
        }
    }
"""

variables = {
    "key": {"name": "first_key", "description": "my very first key"},
    "tenant": "first_tenant"
}

while True:
    callAppsync(mutation, variables=variables)
    sleep(1)
