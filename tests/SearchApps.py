#!/usr/bin/env python3.8
# from appsync import callAppsync
from os import environ
from time import sleep
import json
from urllib.parse import urlparse
import requests
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth
from pprint import pprint

query = """
    query searchApps($tenant: String!, $name: String!) {
      SearchApps(tenant: $tenant, name: $name){
        items {
            ... on ManagedApp {
                name
                nodes {
                    ... on Hl7MllpInboundNode {
                        name
                        sendEdges {
                            name
                            queue
                            kmsKey {
                                name
                                arn
                            }
                        }
                    }
                    ... on Hl7MllpOutboundNode {
                        name
                        receiveEdges {
                            name
                            queue
                            kmsKey {
                                name
                                arn
                            }
                        }
                    }
                }
            }
        }
      }
    }
"""

# variables = {"name": "myfirstapp", "partial_name": True, "tenant": "first_tenant"}
variables = {"tenant": "Joe Wortmann"}

# callAppsync(query, variables=variables)
api = environ["APPSYNC_ENDPOINT"]
region = "us-east-1"
auth = BotoAWSRequestsAuth(aws_host=urlparse(api).hostname, aws_region=region, aws_service="appsync")
headers = {'Content-Type': 'application/graphql'}
data = {'query': query, 'variables': variables}
res = requests.post(api, json=data, auth=auth, headers=headers)
pprint(res)
