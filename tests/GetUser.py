#!/usr/bin/env python3.8
from json import dumps
from appsync import callAppsync


user = """
     query getUser {
         GetUser{
             email
             tenants {
                 name
                 region
             }
         }
     }
"""

try:
    callAppsync(user)
except Exception as e:
    print(e)
