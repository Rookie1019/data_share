from data_opera import Stack



def par_cheacker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def diff_par_cheacker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':    # 这里不同
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()        # 这里不同
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(forward,back):  # 上个函数用到的匹配函数
    forwards = '([{'
    backs = ')]}'
    return forwards.index(forward) == backs.index(back)


def main():

    # print(par_cheacker('((())))'))
    print(diff_par_cheacker('([])'))
    







if __name__ == "__main__":
    main()