#!/usr/bin/env python3.8
from json import dumps
from appsync import callAppsync


node = """
    mutation putNode($tenant: String!, $node: NodeInput!, $receiveMessageType: String!) {
        PutTransNode(tenant: $tenant, node: $node, receiveMessageType: $receiveMessageType, ){
            name
            description
        }
    }
"""


vars = {
    "tenant": "Mathew1",
    "node": {
        "name": "trans node 1",
        "description": "managed node 1",
        "metadata": dumps({})
    },
    "receiveMessageType": "dicom"
}


# try:
#     callAppsync(managed_node_type, variables=node_type_vars)
# except Exception as e:
#     print(e)

try:
    callAppsync(node, variables=vars)
except Exception as e:
    print(e)
