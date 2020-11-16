import file_manage
import sys
import model
import tools
import Student

# # 一定要在外面定义这个全局变量  才能把每一个都加进去
# teacher = {} # 先定义空字典 再一个个加进去
# data = file_manage.read_json('data.json')
def register():

    #data = {}  # 先定义空字典 再一个个加进去
    # 这是更优化的做法  先读取文件内容 就能保证每次都是加进去 而不是一次一个
    data = file_manage.read_json('data.json')
    while True:
        teacher_name = input('请输入账号（3~6位）')
        if not 3 <= len(teacher_name) <= 6:
            print('输入有误，请重新入')
        else:
            break
    if teacher_name in data:
        print('您输入的用户名已经在注册')
        return
    while True:
        password = input('请输入密码（6~12位）')
        if not 6 <= len(password) <= 12:
            print('输入有误，请重新输入')
        else:
            break

    t = model.teacher_list(teacher_name, password)
    data[t.name] = t.passwd
    # data[teacher_name] = password
    # print(teacher)

    file_manage.write_json('data.json',data)  # 真正开发的时候 用到的时数据库

# 全部输入正确之后 需要保存起来 字典

def login():
    # 也要读取文件
    data = file_manage.read_json('data.json')

    while True:
        teacher_name = input('请输入账号: ')
        if teacher_name not in data:
            print('该账号未注册，请重新输入')
            return
        password = input('请输入密码: ')
        if data[teacher_name] == tools.encrypt_password(password): # 和加密好的代码进行比对
            print('登陆成功')
            Student.show_student()
            Student.user_name = teacher_name
        else:
            print('密码错误，登陆失败')



    pass

def start():
    c = file_manage.file_read('welcome.txt')
    while True:
        operator =input(c+'\n请选择1-3  ')
        if operator == '1':
            print('登录')
            login()
        elif operator == '2':
            print('注册')
            register()
        elif operator == '3':
            print('退出')
            # break
            # exit(0)
            sys.exit(0)  # 三种退出方式
        else:
            print('输入有误!')

if __name__ == '__main__':
    start()