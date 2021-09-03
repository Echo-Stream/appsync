#!/usr/bin/env python3.8
from time import time
from json import dumps
from appsync import callAppsync


mutation = """
    mutation putTenant($name: String!, $region: Region!, $billingInfo: AWSJSON!) {
        PutTenant(name: $name, region: $region, billingInfo: $billingInfo){
            name,
            region
        }
    }
"""

# for x in range(1, 10):
#     variables = {
#         "tenant": {"name": f"tenant_{x}", "defaultRegion": "us_east_1", "billingInfo": dumps({})}
#     }
#
#     callAppsync(mutation, variables=variables)

variables = {
    "name": f"Mathew {int(time())}",
    "region": "us_east_1",
    "config": dumps({"foo": "bar"})
}

callAppsync(mutation, variables=variables)
