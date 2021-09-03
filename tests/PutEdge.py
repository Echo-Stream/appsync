#!/usr/bin/env python3.8
from appsync import callAppsync
from time import sleep


mutation = """
    mutation putEdge($tenant: String!, $edge: EdgeInput!) {
        PutEdge(tenant: $tenant, edge: $edge){
            queue
        }
    }
"""

variables = {
    "tenant": "rla - tenant - 1",
    "edge": {
        "source": "router node",
        "target": "trn node 1",
        "description": "mathew test",
        "kmsKey": "DEFAULT_KEY"
    }
}

callAppsync(mutation, variables=variables)
