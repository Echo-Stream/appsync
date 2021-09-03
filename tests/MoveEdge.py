#!/usr/bin/env python3.8
from appsync import callAppsync
from time import sleep


mutation = """
    mutation moveEdge($tenant: String!, $source: String!, $target: String!, $oldSource: String!, $oldTarget: String!) {
        MoveEdge(tenant: $tenant, source: $source, target: $target, oldSource: $oldSource, oldTarget: $oldTarget){
            queue
            source {
                ... on Hl7MllpInboundNode {
                    name
                }
                ... on Hl7MllpOutboundNode {
                    name
                }
            }
            target {
                ... on Hl7MllpInboundNode {
                    name
                }
                ... on Hl7MllpOutboundNode {
                    name
                }
            }
            description
            kmsKey {
                arn
            }
            queue
        }
    }
"""

variables = {
    "tenant": "Mathew",
    "oldSource": "msp cognito sender",
    "oldTarget": "msp cognito sender 2",
    "source": "msp cognito sender",
    "target": "msp cognito sender 3"
}

callAppsync(mutation, variables=variables)
