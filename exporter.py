import fnmatch
import os
import http.server
import socketserver
import time
from datetime import datetime, timedelta

PORT = int(os.getenv('EXPORT_PORT', 8080))
DIR = os.getenv('EXPORT_DIR', "/var/www/html")
FILE_PATTERN = os.getenv('EXPORT_FILE_PATTERN', "*")

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        files = fnmatch.filter(os.listdir(DIR), FILE_PATTERN)
        files_with_sizes_dates_ages = [(f, os.path.getsize(os.path.join(DIR, f)), os.path.getmtime(os.path.join(DIR, f)), time.time() - os.path.getmtime(os.path.join(DIR, f))) for f in files]
        files_with_sizes_dates_ages.sort(key=lambda x: x[2], reverse=True)

        html = '# HELP file_size The size of the file in bytes\n'
        html += '# TYPE file_size gauge\n'
        for f, size, mtime, age in files_with_sizes_dates_ages:
            mtime = datetime.fromtimestamp(mtime)

            if mtime.date() == datetime.today().date():
                html += f'file_size{{name="{f}", date="{mtime}", age="{age}", period="today"}} {size}\n'
            elif mtime.date() == datetime.today().date() - timedelta(days=1):
                html += f'file_size{{name="{f}", date="{mtime}", age="{age}", period="yesterday"}} {size}\n'
            else:
                html += f'file_size{{name="{f}", date="{mtime}", age="{age}", period="previous_days"}} {size}\n'
        self.wfile.write(bytes(html, "utf8"))

handler_object = MyHttpRequestHandler

my_server = socketserver.TCPServer(("", PORT), handler_object)

my_server.serve_forever()
