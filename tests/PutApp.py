#!/usr/bin/env python3.8
from appsync import callAppsync
from time import time

mutation = """
mutation putManagedApp($tenant: String!, $app: AppInput!) {
    PutManagedApp(tenant: $tenant, app: $app){
        name
        description
    }
}
"""

variables = {
    "tenant": "Mathew 1610579950",
    "app": {
        "name": "test systemd",
        "description": "test managed app systemd"
    }
}

callAppsync(mutation, variables)
