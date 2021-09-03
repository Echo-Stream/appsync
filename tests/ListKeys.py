#!/usr/bin/env python3.8

from appsync import callAppsync

query = """
    query listKeys($tenant: String!){
        ListKeys(tenant: $tenant){
            items {
                name,
                arn,
                description,
                tenant { name }
            }
        }
    }
"""

callAppsync(query, {"tenant": "Mathew Refactor"})
