from app import create_app
from livereload import Server

app = create_app()

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('app/templates/*.html')
    server.watch('app/static/style/*.css')
    server.serve(port=5000, debug=True, open_url_delay=True)
    print("ssSSsss")