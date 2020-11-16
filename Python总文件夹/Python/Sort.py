students = [
    {"s": 32, "d": 56},
    {"s": 54, "d": 78},
    {"s": 455, "d": 26},
    {"s": 23, "d": 765}

]



# students = [1,2,3,54,8784,994584]

# def foo(el):
#     return el["s"]

students.sort(key=lambda ele: ele["s"])
print(students)