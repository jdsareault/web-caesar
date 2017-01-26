import webapp2
import string
from crypto import encrypt

form = """<h1>Enter some text to ROT13:</h1>
<form method="post" action="/submit">
    <textarea name="text" rows="6" cols="40">Test</textarea><br><br>
    <input type="submit">
</form>"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
