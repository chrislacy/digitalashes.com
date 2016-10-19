digitalashes.com
================

The full source code for [digitalashes.com][1]. Because independent developers have better things to do than piss about writing company websites.

Currently contains the following pages:
* Index (I list all my apps, and link to where to get them)
* About
* Contact
* Page not found
* Privacy Policy
* Terms of Service

A note of the legal pages
-------------------------

My Privacy Policy and Terms of Service are included in this release, but I make absolutely no guarantees as to the legal suitability of these documents for your own usage.

Usage
-----

This website is built to run on [Google App Engine][2] using the Python 2.7 runtime.

To deploy this application yourself, point a terminal to the `src` folder and enter the following command:
`gcloud app deploy --project=digitalashescom`

Note: if forking this, be sure to use your own unique identifier for project above. 

Full instructions for uploading an AppEngine app can be found [here][3].


Contributions
-------------

If you are skilled with web development and would like to improve this project, I would certainly welcome any and all help in this regard.

The most obvious area lacking at the moment are detailed product pages for individual apps (Link Bubble and Action Launcher are the more important apps).

License
-------

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



All product names, icons, logos and similar including but not limited to Digital Ashes, Action Launcher, Link Bubble and Tweet Lanes are copyright Digital Ashes PTY. LTD. Usage is prohibited without express written permission of Digital Ashes PTY. LTD.


 [1]: http://www.digitalashes.com
 [2]: https://cloud.google.com/appengine/docs
 [3]: https://cloud.google.com/appengine/docs/python/tools/uploadinganapp
