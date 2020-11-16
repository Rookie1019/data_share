import tools


# 老师类
class teacher_list(object):

    def __init__(self,name,passwd):
        self.name = name
        self.passwd = tools.encrypt_password(passwd)  # 调用的时候 加密

class student_list(object):

    def __init__(self,s_id,name,age,gender,tel):
        self.name = name
        self.age = age
        self.gender = gender
        self.tel = tel
        self.s_id = s_id

