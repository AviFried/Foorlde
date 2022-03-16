from gevent.pywsgi import WSGIServer
from main import app
http_server = WSGIServer(('0.0.0.0', 5000), app)
print(http_server.server_host)
http_server.serve_forever()