#!/usr/bin/env python3.8
from appsync import callAppsync
from time import sleep


query = """
    query searchNodes($tenant: String!, $filter: String, $filter_value: String) {
      SearchNodes(tenant: $tenant, filter: $filter, filter_value: $filter_value){
        items {
            ... on Hl7MLLPInboundNode {
                name
                type
                send_edges {
                    name
                }
            }
            ... on Hl7MLLPOutboundNode {
                name
                type
                receive_edges {
                    name
                }
            }
        }
      }
    }
"""

variables = {"tenant": "first_tenant" } #, "filter": "type", "filter_value": "Hl7MLLPInboundNode"}
while True:
    callAppsync(query, variables=variables)
    sleep(2)
