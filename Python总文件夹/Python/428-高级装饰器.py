

def can_play(fn):

    print('外部函数被调用了')

    def inner(name,game,**kwargs):
        clock = kwargs.get('clock',21)
        if clock > 21:
            print('太晚了不能玩游戏')
        else:

            fn(name,game)

    return inner()




@can_play  # 只要有装饰器  函数就会被调用
def play(name,game):
    print(name + '正在玩' + game)

# play('张三','王者荣耀')   直接调用会报错  要给inner函数和被装饰的函数同样的参数