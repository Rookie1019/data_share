import file_manage
import model
import index

user_name = ''  # %s 的功能在index里面实现  在用户输入了用户名的时候保存着


# student_list = []
def add():
    x = file_manage.read_json(user_name + '.json')
    if not x:
        student_list = []
        num = 0
    else:
        student_list = x['all students']
        num = int(x['nums'])

    while True:
        num += 1
        s_id = 'stu' + str(num).zfill(4)
        name = input('请输入姓名: ')
        age = input('请输入年龄: ')
        gender = input('请输入性别: ')
        tel = input('请输入电话: ')

        # 创建student对象
        s = model.student_list(s_id, name, age, gender, tel)

        # student_list = []
        student_list.append(s.__dict__)
        data = {'all students': student_list, 'nums': len(student_list)}  # 自己拼接字典
        # print(data)
        file_manage.write_json(user_name + '.json', data)
        choice = input('添加成功! \n1.继续 \n2.返回 \n请选择（1-2）')
        if choice == '2':
            break


def show():
    key = value = ''
    choice = input('1.查看所有学生 \n2.根据姓名查找 \n3.根据学号查找 \n其他:返回 \n')

    x = file_manage.read_json(user_name + '.json')
    # 这方法太麻烦
    # if not x: 如果文件不存在，是个空列表
    #     student = []
    #     print('您还有没有学生')
    # else:
    #     student = x['all students']
    student = x.get('all students', [])
    if not student:
        print('请添加学生')
        return


    if choice == '1':   # 查询所有学生
        # for k in student:# 格式化列表
        #     print('学号:{s_id},姓名:{name},性别:{gender},年龄:{age},电话{tel}'.format(**k))
        pass


    elif choice == '2':
        # s_name = input('请输入学生姓名: ')
        value = input('请输入学生姓名: ')
        key = 'name'

    elif choice == '3':
        value = input('请输入学号: ')
        # s_id = input('请输入学号')
        key = 's_id'
    else:
        return
    student = filter(lambda s: s.get(key,'') == value,student) # 过滤功能

    if not student:
        print('未找到学院')
        return
    for k in student:  # 格式化列表
         print('学号:{s_id},姓名:{name},性别:{gender},年龄:{age},电话{tel}'.format(**k))

def modify():
    pass


def delete():
    pass


def back():
    pass


def show_student():
    c = file_manage.file_read('student.txt') % user_name
    while True:
        # print(c + '\n')
        s = input(c + '\n请输入1~5  ')
        if s == '1':
            add()
        elif s == '2':
            show()
        elif s == '3':
            pass
        elif s == '4':
            pass
        elif s == '5':
            pass
        else:
            print('输入有误，请重新输入')
