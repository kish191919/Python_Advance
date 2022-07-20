
class Student:

    student_count = 0

    def __init__(self, name, number):
        self._name = name
        self._number = number
        Student.student_count += 1

    def __str__(self):
        return 'str : {} {}'.format(self._name, self._number)

    def __repr__(self):
        return 'repr : {} {}'.format(self._name, self._number)


student1 = Student('danny', 1)
student2 = Student('danny', 1)

# print(student1)
# print(student1.__dict__)

s_list=[]
s_list.append(student1)
s_list.append(student2)
# print(s_list)

print(Student.student_count)

print(id(student1))
print(id(student2))
print(student1._name == student2._name)

a = 'ABC'
b = a

print(id(a))
print(id(b))


print(a)
print(b)

print(id(a))
print(id(b))









