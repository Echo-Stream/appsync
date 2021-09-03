#!/usr/bin/env python3.8
from appsync import callAppsync

query = """
    query searchQueue($search_by: String!, $value: String!) {
      SearchQueues(search_by: $search_by, value: $value){
        name
        url
        tenant {
          name
        }
        kms_key {
          description
        }
      }
    }
"""

variables = {"search_by": "tenant", "value": "first_tenant"}

callAppsync(query, variables=variables)
