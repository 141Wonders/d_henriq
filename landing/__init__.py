
from flask import Flask
import vimeo, uri

app = Flask(__name__)

client = vimeo.VimeoClient(
  token='00806089b46ed18e0b6655aff77bc3ac',
  key='9166539cbc5edc3a5ed3fb41a58fcc71b74776e1',
  secret='qG+peLO+2N6K5k3OiXgqIB6efu3stPkFWfb1ptpkSCCHHnXoU5GupGqeIgDlbgEJXznqEZZg3VZNl3gRXagGny+Rk9yOfjgDtmbYqoymt77CFF4Tquk1MxWS8RbSsHY+'
)

# Make the request to the server for the "/me" endpoint.
about_me = client.get('/me')

# Make sure we got back a successful response.
assert about_me.status_code == 200

# Load the body's JSON data.
print (about_me.json())



from .views import *

