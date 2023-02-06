import pytest
from pytest import fixture
from conftest import *
from base_helpers import *
from user_data import userData
import requests,pytest_schema


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
    )


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Storage:
    userData1 = None
    userData2 = None
    requestId = None
    skipAll = False
    skipAllDummy = False
    failedTestCases = []


basecConfig = None


def pytest_configure(config):
    ENV = config.option.env
    print(ENV)
    global basecConfig
    basecConfig = userData(env=ENV)


# pytest Tests --alluredir=reports -v -s --env dev
# pytest Tests --alluredir=reports -v -s --env staging
# pytest Tests --alluredir=reports -v -s --env preprod
# pytest Tests --alluredir=reports -v -s --env prod
