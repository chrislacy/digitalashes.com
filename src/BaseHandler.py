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
import json
from google.appengine.ext.webapp import template
import webapp2
import logging
import os

#==============================================================================
class BaseHandler(webapp2.RequestHandler):

    #--------------------------------------------------------------------------
    def write_text(self, text):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(text)

    #--------------------------------------------------------------------------
    def write_json(self, data):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(json.dumps(data))

    #--------------------------------------------------------------------------
    def write_html(self, html):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)

    #--------------------------------------------------------------------------
    def write_xml(self, xml):
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.out.write(xml)

    #--------------------------------------------------------------------------
    def write_html_file(self, html_file):
        try:
            html_file_path = os.path.join(os.path.dirname(__file__), html_file)
            f = open(html_file_path)
            self.write_html(f.read())
            f.close()
        except Exception, e:
            logging.exception(e)

    #--------------------------------------------------------------------------
    def write_template(self, template_file, template_data=None):
        """Write a template as output"""

        html = self.render_template(template_file, template_data)

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(html)

    #--------------------------------------------------------------------------
    def render_template(self, template_file, template_data=None):
        """ Given a template, get the resulting HTML.

            Does **NOT** write the html. Use write_template for that.
        """
        template_path = os.path.join(os.path.dirname(__file__), template_file)

        if template_data is None:
            template_data = {}

        #self.append_common_template_data(template_data)

        html = template.render(template_path, template_data)
        return html
