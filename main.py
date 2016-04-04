
import webapp2
import os
import logging
import jinja2
from google.appengine.api import mail


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class AboutHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    	self.response.write(template.render())

class HomeHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/home.html')
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
        template = JINJA_ENVIRONMENT.get_template('templates/subscribed.html')

        userMail=self.request.get("email")
        name=self.request.get("subscription")
        message=mail.EmailMessage(sender="haoliang@umich.edu",subject="Weekly Email Newsletter")

        # not tested
        if not mail.is_email_valid(userMail):
            self.response.out.write("Wrong email! Check again!")

        message.to = userMail
        message.body ="""Thank you for subscribing!
            You have entered following information:
            Your mail: %s
            
            I will keep you updated!
            """ %(userMail)
        message.send()

        self.response.out.write(template.render())


class ErrorHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/error.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/' , HomeHandler),
    ('/about.html', AboutHandler),
    ('/home.html', HomeHandler),
    ('/gallery.html', GalleryHandler),
    ('/contact.html' , ContactHandler),
    ('/.*', ErrorHandler)
], debug=True)


