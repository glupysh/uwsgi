# локальный запуск на порту 8080: uwsgi --http :8080 --wsgi-file foobar.py


from urllib.parse import unquote


def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]
    body = {
        '/': "<h1>Hello, world!</h1>",
        '/about': "<h1>It's me :)</h1>",
        '/say_hello': "<form method='post'><h1>Your name:</h1><input type='text' name='name'><button type='submit'>Enter</button></form>",
        '404': "<h1>Page not found :(</h1>"
    }
    path = environ.get('PATH_INFO', '/')
    if path in body:
        start_response('200 OK', headers)
        name = environ['wsgi.input'].read()
        if name:
            name = unquote(name.decode("utf-8").split('=')[1])
            hello = f"<h1>Hello, {name}!</h1>"
            return [hello.encode('utf-8')]
        return [body[path].encode('utf-8')]
    else:
        start_response('100 NOT OK', headers)
        return [body['404'].encode('utf-8')]
