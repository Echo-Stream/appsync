#!/usr/bin/env python3.8
from json import dumps
from appsync import callAppsync

mutation = """
    mutation Notification(
        $tenant: String!,
        $data: AWSJSON,
        $function: String!
    ) {
        StreamNotifications(
            tenant: $tenant,
            data: $data,
            function: $function
        ) {
            tenant
            message
            error
            item_type
            event_name
            function
            old_record
            new_record
        }
    }
"""
opts = {
    "old_record": None,
    "new_record": None,
    "event_name": "MODIFY",
    "item_type": "N",
    "message": ["foo", "bar", "baz"],
    "error": None
}

function_name = "manage-nodes"

tenant = "first_tenant"

variables = {"data": dumps(opts), "tenant": tenant, "function": function_name}

callAppsync(mutation, variables=variables)
