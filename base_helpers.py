import random
import string
import allure
import pytest
from conftest import *
import requests
import json


def checkInternalServerError(resp):
    print(resp)
    if resp['message'] == 'Internal server error':
        pytest.skip("Skipping Test Case due to Internal Server Error")


def checkAuthFailureSkipAll():
    if Storage.skipAll is True:
        pytest.skip(
            f'Skipping Test Case due to Failed TestCases :{Storage.failedTestCases}')


def get_randomEmail():
    return ''.join(random.choice(string.ascii_letters) for _ in range(15)) + "1421@gmail.com"


def get_randomUsername():
    return ''.join(random.choice(string.ascii_letters) for _ in range(15)) + "1243"


@allure.step("Enter Payload{0}")
def enter_payLoad(payload):
    return payload
