from wsgiref.simple_server import make_server
import webbrowser

def demo_app(environ,start_response):
    status_code = '200 OK'
    response = ''
    path = environ['PATH_INFO']
    if path == '/':
        response = '欢迎来到首页'
    elif path == '/register':
        response = '欢迎注册 廖若雯吗'
    elif path == '/login':
        response = '欢迎登陆 廖若雯'
    else:
        response = '页面丢失'
        status_code = '404 Not Found'
    start_response(status_code, [('Content-Type', 'text/html;charset=utf8')])
    return [response.encode('utf8')]

if __name__ == '__main__':
    httpd = make_server('',12138,demo_app)
    sa = httpd.socket.getsockname()
    print("servering HTTP on",sa[0],'port',sa[1],'...')
    httpd.serve_forever()



