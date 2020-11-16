import json



base_dir = './flie_manage/'   # 如果以后有了新的文件夹 可以在操作的.py文件中更改这个参数就可以了

# 读文件
def file_read(file_name):
    try:
        with open(base_dir+file_name,'r',encoding='utf8') as file:
            content = file.read()
            return content

    except FileNotFoundError:
        print('文件未找到')


# 写入json文件
def write_json(file_name,data):

    with open(base_dir+file_name,'w',encoding='utf8') as file:
       json.dump(data,file)


def read_json(file_name, default_data = {}):
    try:
        with open(base_dir+file_name,'r',encoding='utf8') as file:
            # content = file.read()
            return json.load(file)   # 注意load 不是loads

    except FileNotFoundError:
        # print('文件未找到')
        # 返回一个默认值
        return default_data