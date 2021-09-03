#!/usr/bin/env python3.8
from time import time
from json import dumps
from appsync import callAppsync


mutation = """
    mutation createTenant($name: String!, $region: Region!, $config: AWSJSON) {
        CreateTenant(name: $name, region: $region, config: $config){
            name,
            region
        }
    }
"""

variables = {
    "name": "Mathew - test account 1",
    "region": "us_east_1",
    "config": dumps({"foo": "bar"})
}

callAppsync(mutation, variables=variables)
