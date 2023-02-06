from conftest import *
# from pytest_schema import schema, exact, like
import os

# below is the dummy testcase remove it to start writing your own without having to worry about the configurations wink :wink:


# @allure.epic("Authentication of Website")
# @allure.feature("Register User")
# @allure.story("Test Register Api")
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.description("""
# Scenario: Test Register Api
# Given New User For Registration
# User Data:
# | email | password | first_name | last_name | gender | date_of_birth | username | profile_picture   |
# -------------------------------------------------------------------------------------------------------
# | ah@gmail.com | passypass |   Hassan   |   Abbas   |   1    |   1992-18-01    | hassan  | "path/to/picture" |
# When Set Post Register Api with user data
# Then new account should be created with message "Account created successfully" in Response
# And 200 in HTTP Response code
# Then I get OTP on Email
# """)
# # @allure.testcase(data.register_url, "Registration Api url")
# @pytest.mark.order(2)
# @pytest.mark.parametrize("URL",
#                          [pytest.param("https://www.facebook.com", id="facebook"),
#                           pytest.param("https://www.google.com", id="google"),
#                              pytest.param("https://www.youtube.com", id="youtube")]
#                          )
# def test_visitSite(URL):
#     print(basecConfig.email)
#     requests.get("https://jsonplaceholder.typicode.com/posts")


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
    # print(os.getcwd())



# def getSchemafromJSON(filename):
#     json.load(os.getcwd()/Schema/test1)