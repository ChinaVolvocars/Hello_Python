class Student(object):
    pass


s = Student()
# print s
#
# print Student


# s.name='Bart ssss'
# print s.name

class SS(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


ss = SS('Tiger', 55)
print ss.name, ss.score


def print_score(std):
    print '%s:%s' % (std.name, std.score)


insaa=print_score(SS('TTT',111))
print insaa
