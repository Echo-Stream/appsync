#!/usr/bin/env python3.8
from json import dumps
from appsync import callAppsync


node = """
    mutation putNode($tenant: String!, $app: String!, $node: NodeInput!, $managedNodeType: String!, $portMappings: [PortMappingInput!], $config: AWSJSON!) {
        PutManagedNode(tenant: $tenant, app: $app, node: $node, managedNodeType: $managedNodeType, portMappings: $portMappings, config: $config){
            name
            description
        }
    }
"""


vars = {
    "tenant": "Mathew 1610579950",
    "app": "test systemd",
    "node": {
        "name": "managed node 1",
        "description": "managed node 1",
        "metadata": dumps({}),
    },
    "config": dumps({}),
    "managedNodeType": "hl7-mllp-inbound-node",
    "portMappings": [{
        "hostPort": 2575,
        "containerPort": 2575
    }]
}


# try:
#     callAppsync(managed_node_type, variables=node_type_vars)
# except Exception as e:
#     print(e)

try:
    callAppsync(node, variables=vars)
except Exception as e:
    print(e)
