import os


file_name = input('请输入要复制的文件名  \n')

if os.path.isfile(file_name):

    file = open(file_name,'rb')
    # x = file.read()
    name = file_name.rpartition('.')  # ('xxx', '.', 'txt')  元组 rpartation就是在右边

    new_name = name[0] + ' bak.' + name[2]
    new_file = open(new_name,'wb')

    while True: #  读一点写一点
        # print(name)
        content = file.read(1024)
        new_file.write(content)
        if content == '':
            break

    new_file.close()
    file.close()
else:
    print('输入的文件不存在')