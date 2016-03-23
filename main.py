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
import os
import logging
import jinja2
from google.appengine.api import mail

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class AboutHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    	self.response.write(template.render())

class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.write(template.render())

class GalleryHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/gallery.html')
    	self.response.write(template.render())

class ContactHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
    	self.response.write(template.render())

    def post(self):
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        user_address = str(self.request.get("email"))

        # if not mail.is_email_valid(user_address):
        #     #so something
        #     logging.info("hi")
        # else:
        logging.info("got it")
        # confirmation_url = createNewUserConfirmation(self.request)
        sender_address = str('haoliangc96@gmail.com')
        subject = "Confirm your registration"
        body = "Thank you for filling this form out. Click on link below"
        logging.info(sender_address)
        logging.info(user_address)
        mail.send_mail(sender_address, user_address, subject, body)
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/about.html', AboutHandler),
    ('/index.html', IndexHandler),
    ('/gallery.html', GalleryHandler),
    ('/contact.html' , ContactHandler)
], debug=True)