#!/usr/bin/env python3.8
from json import dumps
from appsync import callAppsync

qry = """
    mutation subscribe($tenant: String!, $endpoint: String!, $protocol: SnsSubscriptionProtocol!) {
        SubscribeToSns(tenant: $tenant, endpoint: $endpoint, protocol: $protocol){
            protocol
            arn
            endpoint
        }
    }
"""


vars = {
    "tenant": "Mathew1",
    "protocol": "email",
    "endpoint": "mmoon@quinovas.com"
}

try:
    callAppsync(qry, variables=vars)
except Exception as e:
    print(e)
