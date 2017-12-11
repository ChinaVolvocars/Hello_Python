# encoding=UTF-8

class Student(object):
    pass


bart = Student()

print bart

print Student

# 给实例变量绑定属性，比如给bart绑定一个name属性
bart.name = 'yuexiaohui'
print bart.name


#
class Study(Student):
    def __init__(self, name, score):
        self.name = name
        self.score = score


study = Study("XIAO MING", 22)
print study.score
print study.name
print ('%s:%s' % (study.name, study.score))


# 数据封装

def print_study(Study):
    print ('%s:%s' % (Study.name, Study.score))


print print_study(study)
