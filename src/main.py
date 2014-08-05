from BaseHandler import BaseHandler
import webapp2
import appdef

#==============================================================================
class PrivacyHandler(BaseHandler):

    def get(self):
        self.write_template(appdef.TEMPLATE_ROOT_PATH + 'privacy_policy.html', None)

#==============================================================================
class TermsHandler(BaseHandler):

    def get(self):
        self.write_template(appdef.TEMPLATE_ROOT_PATH + 'terms.html', None)

#==============================================================================
class PageNotFoundHandler(BaseHandler):

    def get(self):
        self.write_html_file(appdef.TEMPLATE_ROOT_PATH + 'page_not_found.html')

#==============================================================================
class AboutHandler(BaseHandler):

    def get(self):
        self.write_html_file(appdef.TEMPLATE_ROOT_PATH + 'about.html')

#==============================================================================
class ContactHandler(BaseHandler):

    def get(self):
        self.write_html_file(appdef.TEMPLATE_ROOT_PATH + 'contact.html')

#==============================================================================
class MainPage(BaseHandler):

    def get(self):
        self.write_html_file(appdef.TEMPLATE_ROOT_PATH + 'index.html')

#==============================================================================
application = webapp2.WSGIApplication([('/privacy', PrivacyHandler),
                                       ('/terms', TermsHandler),
                                       ('/about', AboutHandler),
                                       ('/contact', ContactHandler),
                                       ('/', MainPage),
                                       ('/.*', PageNotFoundHandler)],
                                      debug=True)
