# USER_PERMISSION = 12 # 1011
# USER_PERMISSION = 17
USER_PERMISSION = 13

# 权限因子
# 权限因子 & 用户权限 != 0
DEL_PERMISSION = 8 # 1000 & 1011 ==>1000
READ_PERMISSION = 4 # 0100 & 1011 ==>0000
WRITE_PERMISSION = 2 # 0010 & 1011 ==>0010
EXE_PERMISSION = 1 # 0001 & 1011 ==>0001

def check_permission(x,y):
    def handle_action(fn):
        def do_action():
            if x & y != 0: # 有权限 可以执行
                fn()

            else:
                print('对不起，您没有访问权限')

        return do_action # 这里不加括号  而且注意缩进
    return handle_action


@check_permission(USER_PERMISSION,READ_PERMISSION)
def read():
    print('正在读内容')

@check_permission(USER_PERMISSION,WRITE_PERMISSION)
def write():
    print('正在写内容')

@check_permission(USER_PERMISSION,DEL_PERMISSION)
def delete():
    print('正在删除内容')

@check_permission(USER_PERMISSION,EXE_PERMISSION)
def execute():
    print('正在执行内容')


read()
write()
delete()
execute()


