from base_helpers import *


class userData:
    def __init__(self, env):
        self.email = get_randomEmail()
        self.password = "passypasss"
        self.newPassword = "passypass"
        self.first_name = "Hassan"
        self.last_name = "Abbas"
        self.gender = "1"
        self.date_of_birth = "1991-21-03"
        self.username = get_randomUsername()
        # self.img_path = os.getcwd() + "/../data/img.jpg"
        # self.profile_picture

        # tokens

        self.access_token = ""
        self.email_verification_token = ""
        self.password_reset_token = ""

        # Base Urls

        self.Auth_base_url = "https://dev.dummyservices.url.google.com" if env == "dev" else "https://staging.dummyservices.url.google.com" if env == "stag" else "https://prod.dummyservices.url.google.com" if env == "prod" else "https://preprod.dummyservices.url.google.com"
        self.Profile_base_url = "https://dev.profile.url.google.com" if env == "dev" else "https://staging.profile.url.google.com" if env == "stag" else "https://prod.profile.url.google.com" if env == "prod" else "https://preprod.profile.url.google.com"
        self.Friends_base_url = "https://dev.friends.url.google.com" if env == "dev" else "https://staging.friends.url.google.com" if env == "stag" else "https://prod.friends.url.google.com" if env == "prod" else "https://preprod.friends.url.google.com"
        self.Chat_base_url = "https://dev.chat.url.google.com" if env == "dev" else "https://staging.chat.url.google.com" if env == "stag" else "https://prod.chat.url.google.com" if env == "prod" else "https://preprod.chat.url.google.com"

        # Authentication urls
        self.demo_url = self.Auth_base_url + '/url/auth/demo-user'
        self.login_url = self.Auth_base_url + "/url/auth/login"
        self.register_url = self.Auth_base_url + "/url/auth/register"
        self.verifyEmail_url = self.Auth_base_url + "/url/auth/verify-email"
        self.verifyUserName_url = self.Auth_base_url + "/url/auth/verify-username"
        self.requestPassword_url = self.Auth_base_url + "/url/auth/request-password"
        self.resetPassword_url = self.Auth_base_url + "/url/auth/reset-password"
        self.OTP_url = self.Auth_base_url + "/url/auth/get-verification-code"
        self.resendEmail_OTP_url = self.Auth_base_url + \
            "/url/auth/resend-email-verification-token"

        # profile Urls

        self.getProfile_url = self.Profile_base_url + '/url/get-profile'
        self.updateProfile_url = self.Profile_base_url + '/url/update-profile'
        self.searchUsers_url = self.Profile_base_url + '/url/search-users'
        self.viewOtherUserProfile_url = self.Profile_base_url + '/url/view-user-profile'

        # Friends Urls

        self.sendFriendRequest_url = self.Friends_base_url + '/url/send-request'
        self.viewMyFriends_url = self.Friends_base_url + '/url/view-my-friends'
        self.viewOthersFriends_url = self.Friends_base_url + '/url/view-other-friends'
        self.AcceptRejectFriendRequest_url = self.Friends_base_url + \
            '/url/accept-or-reject-request'
        self.seeFriendRequest_url = self.Friends_base_url + '/url/view-received-requests'
        self.unFriendUser_url = self.Friends_base_url + '/url/unfriend-user'

        # Chat Urls

        self.getAllGroups = self.Chat_base_url + '/url/get-all-groups'
        self.getGroupMessages = self.Chat_base_url + '/url/get-group-messages'
        self.createGroup = self.Chat_base_url + '/url/create-group'
        self.makeAdmin = self.Chat_base_url + '/url/make-admin'
        self.removeAdmin = self.Chat_base_url + '/url/remove-admin'
        self.getGroupDetails = self.Chat_base_url + '/url/get-group-details'

        # url Response Time = 1 sec
        self.reqTime = 30

    def time_exception(self, time):
        assert time < self.reqTime, "LoadTimeError"
