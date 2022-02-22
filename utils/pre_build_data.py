"""
author:wanhongda
time:2022.02.21
function:
    公共方法模块
"""
import pytest

from utils import GameTestUtils
from utils.ByteTracker import ByteTracker
import requests
import urllib


from utils import yaml_control



def pre_build(params):
    body = GameTestUtils.request_generate(params)
    url_encode_message = urllib.parse.quote(body)
    body = 'v=' + url_encode_message
    return body
