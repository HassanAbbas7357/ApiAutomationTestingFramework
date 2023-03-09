import random
import string
import allure
import pytest
from conftest import *
import requests
import json
import os
import jsonschema


@allure.step("checkInternalServerError")
def checkInternalServerError(resp):
    print(resp)
    if resp['message'] == 'Internal server error':
        pytest.skip("Skipping Test Case due to Internal Server Error")


@allure.step("checkAuthFailureSkipAll")
def checkAuthFailureSkipAll():
    if Storage.skipAll is True:
        pytest.skip(
            f'Skipping Test Case due to Failed TestCases :{Storage.failedTestCases}')


@allure.step("get_randomEmail")
def get_randomEmail():
    return ''.join(random.choice(string.ascii_letters) for _ in range(15)) + "1421@gmail.com"


@allure.step("get_randomUsername")
def get_randomUsername():
    return ''.join(random.choice(string.ascii_letters) for _ in range(15)) + "1243"


@allure.step("Enter Payload {0}")
def enter_payLoad(payload):
    return payload


@allure.step("getSchemafromJSONAndCompareSchema")
def getSchemafromJSONAndCompareSchema(JsonResp, filename):
    filepath = os.getcwd()+'/Schemas/'+filename
    with open(filepath, 'r') as f:
        schema = json.load(f)

    try:
        jsonschema.validate(JsonResp, schema)
    except Exception as ex:
        pytest.fail(f'Test Failed due Schema mismatched {ex}')

