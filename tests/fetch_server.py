#!/usr/bin/env python3.8
from cognitoinator import TokenFetcher
from logging import getLogger, StreamHandler
from sys import stdout
from os import path

getLogger().addHandler(StreamHandler(stdout))
getLogger().setLevel("CRITICAL")
getLogger("cognitoinator").setLevel("CRITICAL")
getLogger("cognitoinator").addHandler(StreamHandler(stdout))
getLogger("boto3").setLevel("CRITICAL")
getLogger("botocore").setLevel("CRITICAL")
getLogger("urllib3").setLevel("CRITICAL")


TokenFetcher(token_cache=f"{path.expanduser('~')}/.cognito_token_cache", server=True, non_blocking=False)
