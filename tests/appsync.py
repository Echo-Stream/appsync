#!/usr/bin/env python3.8
from time import time
import logging
from sys import stdout
from os import environ, path
from json import loads
from pprint import pformat
import datetime
import requests
from cognitoinator.providers import TokenFetcher

logLevels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "ERROR": logging.ERROR
}

logLevel = environ.get("LOG_LEVEL") or "INFO"
logging.basicConfig(level=logLevels[logLevel], stream=stdout)
logger = logging.getLogger()
fetcher = TokenFetcher(token_cache=f"{path.expanduser('~')}/.cognito_token_cache")

id_token = fetcher.id_token


def callAppsync(query, variables={}, endpoint=environ.get("APPSYNC_ENDPOINT")):
    headers = {
        'Content-Type': 'application/graphql',
        'Authorization': id_token,
        'X-Amz-Date': str(datetime.datetime.now().isoformat())
    }
    start = time()
    data = {'query': query, 'variables': variables}
    res = loads(requests.post(endpoint, json=data, headers=headers).content.decode())
    if "errors" in res and res["errors"]:
        logger.info(res["errors"])
    else:
        if isinstance(res, list):
            count = len(res["data"][list(res["data"].keys())[0]])
        else:
            count = ""
        logger.info(f"Query returned {count} results in {time() - start} seconds.")
        logger.info(pformat(res))
    return res
