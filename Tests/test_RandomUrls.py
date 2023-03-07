from conftest import *
import jsonschema
import os
import allure
from base_helpers import *


@allure.step("Capture Page")
def capturePage():
    pass


@allure.epic("Authentication of Website")
@allure.feature("Register User")
@allure.story("Test Register Api")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
Scenario: Test Register Api
Given New User For Registration
User Data:
| email | password | first_name | last_name | gender | date_of_birth | username | profile_picture   |
-------------------------------------------------------------------------------------------------------
| ah@gmail.com | passypass |   Hassan   |   Abbas   |   1    |   1992-18-01    | hassan  | "path/to/picture" |
When Set Post Register Api with user data
Then new account should be created with message "Account created successfully" in Response
And 200 in HTTP Response code
Then I get OTP on Email
""")
# @allure.testcase(data.register_url, "Registration Api url")
@pytest.mark.order(1)
def test_visitSite():
    print(basecConfig.email)
    resp = requests.get("https://jsonplaceholder.typicode.com/posts").json()

    print(resp)
    print(type(resp))
    capturePage()
    getSchemafromJSONAndCompareSchema(resp, "test1_schema.json")
    capturePage()

    # print(os.getcwd())
