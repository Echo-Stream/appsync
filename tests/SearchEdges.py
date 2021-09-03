#!/usr/bin/env python3.8
from appsync import callAppsync
from time import sleep
query = """
    query searchEdges($source: String, $target: String) {
      SearchEdges(source: $source, target: $target){
        items {
          name
          source {
            .. on Hl7MLLPInboundNode {
                name
            }
            .. on Hl7MLLPInboundNode {
                name
            }
          }
          target {
            .. on Hl7MLLPInboundNode {
                name
            }
            .. on Hl7MLLPInboundNode {
                name
            }
          }
        }
      }
    }
"""

query = """
    query searchEdges($source: String, $tenant: String!) {
        SearchEdges(source: $source, tenant: $tenant){
            items {
                name
                source {
                    ... on Hl7MLLPInboundNode {
                        name
                    }
                    ... on Hl7MLLPOutboundNode {
                        name
                    }
                }
                target {
                    ... on Hl7MLLPInboundNode {
                        name
                    }
                    ... on Hl7MLLPOutboundNode {
                        name
                    }
                }
            }
        }
    }
"""

while True:
    variables = {"source": "mllp_in", "tenant": "first_tenant"}
    callAppsync(query, variables=variables)
    sleep(2)
