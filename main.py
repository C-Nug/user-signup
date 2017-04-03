#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#  *** Created by C-Nug for LC101 ***
#
import webapp2
import re
import cgi


head = """
    <!DOCTYPE HTML>
    <html>
    <head>
        <title>User Signup</title>
        <style>
            body {
              background-color: #edcabb;
              font-family: Sans-serif;
              font-size: 18px;
            }
            .error_style {
              color: red;
              font-size: .75em;
            }
            .center {
              margin: 0;
              position: absolute;
              top: 40%;
              left: 50%;
              transform: translate(-50%, -50%);
            }
        </style>
    </head>

    <body>
"""

foot = """
    </body>
    </html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        error_message = self.request.get("error")
        username = self.request.get("username")
        username_error = ""
        password_error = ""
        verifypassword_error = ""
        email_error = ""

        # Converts codes to messages
        if "e812" in error_message:
            username_error = "You forgot to enter a name ya dummy!"
        elif "e813" in error_message:
            username_error = "Invalid username"
        if "e814" in error_message:
            password_error = "Password must be 6 to 20 characters long"
        if "e815" in error_message:
            verifypassword_error = "Passwords do not match"
        if "e816" in error_message:
            email_error = "Invalid email"

        #TODO: make forms remember input upon refresh
        # HTML for user form
        form = """
            <form action="newuser" method="post">
                <table class="center">
                    <tr>
                        <td>
                            <h2>Sign up</h2>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>Username</label>
                        </td>
                        <td>
                            <input type="text" name="username" value="{4}">
                        </td>
                        <td class="error_style">
                            {0}
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>Password</label>
                        </td>
                        <td>
                            <input type="password" name="password">
                        </td>
                        <td class="error_style">
                            {1}
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label>Verify Password</label>
                        </td>
                        <td>
                        <input type="password" name="passwordverify">
                        </td>
                        <td class="error_style">
                            {2}
                        </td>
                    </tr>
                        <td>
                            <label>Email (optional)</label>
                        </td>
                        <td>
                            <input type="text" name="email">
                        </td>
                        <td class="error_style">
                            {3}
                        </td>
                    <tr>
                        <td>
                        </td>
                        <td>
                            <input type="submit">
                        </td>
                    </tr>
                </table>
            </form>
        """.format(username_error, password_error,
                    verifypassword_error, email_error,
                    username)


        self.response.write(head + form + foot)

class UserAddedHandler(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        passwordverify = self.request.get("passwordverify")
        email = self.request.get("email")

        welcome = """
            <h2 class="center">Welcome to The Rock, {0}!</h2>
        """.format(username)

        # Valid form expressions
        user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        password_re = re.compile(r"^.{6,20}$")
        email_re = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

        # Handles all error messages with e### codes
        error_code = ""
        if username == "":
            error_code += "e812"
        if not user_re.match(username):
            error_code += "e813"
        if not password_re.match(password):
            error_code += "e814"
        if password != passwordverify:
            error_code += "e815"
        if not email_re.match(email) and email != "":
            error_code += "e816"

        if error_code != "":
            self.redirect("/?error=" + error_code)
        else:
            self.response.write(head + welcome + foot)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/newuser', UserAddedHandler)],
    debug=True)
