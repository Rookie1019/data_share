
class student(object):

    def __init__(self,number,name,age,gender,code):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.code = code

class grade(object):

    def __init__(self,grade_name,members):
        self.grade_name = grade_name
        self.members = members

    def show_all(self):
        for student in self.members:
            print()

