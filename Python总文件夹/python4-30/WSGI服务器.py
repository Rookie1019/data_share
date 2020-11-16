# import wsgiref
from wsgiref.simple_server import make_server
import webbrowser


def demo_app(x,y): # 用户的请求处理函数
    y('200 OK',[('Content-Type','text/html;charset=utf8')])
    return ['陶凤磊'.encode('utf8')]
    # pass

if __name__ == '__main__':
    # demo_app是一个函数 用来处理用户的请求的
    # with make_server('',8000,demo_app) as httpd:
    #     and
    httpd = make_server('',12138,demo_app)
    sa = httpd.socket.getsockname()
    print("servering HTTP on",sa[0],'port',sa[1],'...')
    httpd.serve_forever()
    #httpd.handle_request()
    webbrowser.open('https://www.bilibili.com/video/BV1D7411P7oz/?p=20&t=80')
