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
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        html = """
        <html>
        <header>
            <title>User Signup</title>
        </head>

        <body>
            <h2>Sign up</h2>
            <form method="post">
                <div>
                    <label>Username</label>
                    <input type="text" name="username">
                </div>
                <div>
                    <label>Password</label>
                    <input type="text" name="password">
                </div>
                <div>
                    <label>Verify Password</label>
                    <input type="text" name="passwordverify">
                </div>
                <div>
                    <label>Email (optional)</label>
                    <input type="text" name="email">
                </div>
                <div>
                    <input type="submit">
                </div>
            </form>
        </body>
        </html>
        """

        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
