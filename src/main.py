import http.server
import socketserver
import os

PORT = 8080
WEB_DIR = os.path.join(os.path.dirname(__file__), 'www')
os.chdir(WEB_DIR)

Handler = http.server.SimpleHTTPRequestHandler

print("Сервер запущен на http://localhost:8080")
print("Для остановки нажмите Ctrl + C")

# Запускаем сервер без лишних отступов
httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()
