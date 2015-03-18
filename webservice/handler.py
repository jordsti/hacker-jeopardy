__author__ = 'jguerin'
import BaseHTTPServer
import json
import service_func


class service_handler(BaseHTTPServer.BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        BaseHTTPServer.BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_GET(self):
        data = None
        uri_splitted = self.path.split('?')
        path = uri_splitted[0]
        args = {}

        print "Serving request : %s:%d, URI : %s" % (self.client_address[0], self.client_address[1], self.path)

        if len(uri_splitted) > 1:
            url_args = uri_splitted[1].split('&')

            for a in url_args:
                a_data = a.split('=')
                a_name = a_data[0]
                a_value = None
                if len(a_data) > 1:
                    a_value = a_data[1]
                args[a_name] = a_value

        for f in self.server.functions:
            if path == f.func_path:
                try:
                    f.init()
                    f.execute(args, self.server)
                    data = f.answer()
                except KeyError:
                    data = {"error": "Missing argument"}
                except service_func.func_error as f_e:
                    data = {"func_error": str(f_e)}

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if data is not None:
            self.wfile.write(json.dumps(data))
        else:
            data = {"error": "Unknown function"}
            self.wfile.write(json.dumps(data))