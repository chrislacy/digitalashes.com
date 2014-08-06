'''
Copyright 2014 Chris Lacy.

    Licensed under the MIT License.
    You may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://opensource.org/licenses/MIT

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''

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
