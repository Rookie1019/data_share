import hashlib

def encrypt_password(passwd,x = 'sadjansdnaksfuhasjkdka'):
    '''

    :param passwd:密码
    :param x:随机字符串
    :return:加密密码得模块
    '''

    h = hashlib.sha256()
    h.update(passwd.encode('utf8'))
    h.update(x.encode('utf8'))
    return h.hexdigest()