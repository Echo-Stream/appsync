#!/usr/bin/env python3.8
from appsync import callAppsync

mutation = """
    mutation putNode($app: String!, $tenant: String!, $node: NodeInput!, $sendMessageType: String!, $receiveMessageType: String!) {
        PutExternalNode(app: $app, tenant: $tenant, node: $node, sendMessageType: $sendMessageType, receiveMessageType: $receiveMessageType){
            name
            description
            tenant {
                name
            }
        }
    }
"""

variables = {
    "tenant": "Mathew",
    "node": {
        "name": "msp cognito sender 3",
        "description": "3"
    },
    "sendMessageType": "hl7",
    "receiveMessageType": "hl7",
    "app": "External cognito"
}

callAppsync(mutation, variables=variables)
