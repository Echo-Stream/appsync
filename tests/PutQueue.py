#!/usr/bin/env python3.8
from appsync import callAppsync

mutation = """
mutation putQueue($queue: QueueInput!) {
    PutQueue(queue: $queue){
        name
        url
    }
}
"""

variables = {
    "queue": {
        "name": "queue1",
        "kms_key": "my_third_key"
    }
}


callAppsync(mutation, variables=variables)
