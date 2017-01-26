import webapp2
import cgi
from crypto import encrypt

form = """<h1>Enter some text to ROT13:</h1>
<form method="post" action="/">
    <textarea name="text" rows="6" cols="40">%(message)s</textarea><br><br>
    <input type="submit">
</form>"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self, message=""):
        self.response.write(form % {"message": message})

    def get(self):
        self.write_form()

    def post(self):
        encrypted_message = encrypt(self.request.get("text"),13)
        sanitized_message = cgi.escape(encrypted_message, True)
        self.write_form(sanitized_message)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
