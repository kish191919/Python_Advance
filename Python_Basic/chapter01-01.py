

# 학생1
student_name_1 = 'Kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
    {'gender': 'Male'},
    {'score1': 95},
    {'score2': 88}
]

# 학생2
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
    {'gender': 'Female'},
    {'score1': 77},
    {'score2': 92}
]

# 학생3
student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = [
    {'gender': 'Male'},
    {'score1': 99},
    {'score2': 100}
]

# 리스트 구조
# 코드 반복, 인덱스로 삭제
student_names_list = ['Kim', 'Lee','Park']
student_numbers_list = [1,2,3]
student_grades_list = [1,2,4]
student_details_list = [
    {'gender': 'Male', 'score1': 95, 'score2': 88},
    {'gender': 'Female','score1': 77, 'score2': 92 },
    {'gender': 'Male', 'score1': 99, 'score2': 100 }
]

# 학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

print()
print()

# 딕셔너리 구조 / json array 구조
# 코드 반복, 중첩 문제, 인덱스로 제거
students_dicts = [
    {'student_name' : 'kim', 'student_number':1, 'student_grade' : 1, 'student_detail': {'gender': 'Male', 'score1': 95, 'score2': 88 }},
    {'student_name' : 'Lee', 'student_number':2, 'student_grade' : 2, 'student_detail': {'gender': 'Female', 'score1': 77, 'score2': 92 }},
    {'student_name' : 'Park', 'student_number':3, 'student_grade' : 4, 'student_detail': {'gender': 'Male', 'score1': 99, 'score2': 100 }},
]

del students_dicts[1]
print(students_dicts)
print()
print()
# 외부에 있는 프로그램을 서드 파티라고 함
# 외부 프로그램을 다운로드받으면 딕셔너리 형식이 많음

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드

class Student(object):
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    # 클래스를 만들때는 str 이나 repr을 사용해서 입력된 변수가 무엇인지 나오게 만드는게 좋다
    # 이 메소드들이 없으면 디버깅할때 어떠한 값이 들어갔는지 확인하기가 힘듦
    def __str__(self): #프린트할때 입력 변수를 보여줌
        return 'str: {}'.format(self._name)

    def __repr__(self):
        return 'repr: {}'.format(self._name)

student1 = Student('Kim', 1, 1, {'gender': 'Male', 'score1': 95, 'score2': 88 })
student2 = Student('Lee', 2, 2, {'gender': 'Female', 'score1': 77, 'score2': 92})
student3 = Student('Park', 3, 4, {'gender': 'Male', 'score1': 95, 'score2': 88 })

print(student1.__dict__) # 네임스페이스 안에 속성값이 나타남
print(student2.__dict__) # 네임스페이스 안에 속성값이 나타남
print(student3.__dict__) # 네임스페이스 안에 속성값이 나타남

# 리스트 선언
students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student2)

print()
print(students_list) #객채가 나타남

for x in students_list:
    print(repr(x)) # 강제로 repr을 나타나게 함
    print(x)

'''
str: Kim
str: Lee
str: Lee
'''

'''
만약 str 함수가 없다면
<__main__.Student object at 0x10b859c10>
<__main__.Student object at 0x10b859b90>
<__main__.Student object at 0x10b859b90>
'''

'''
만약 str 함수가 없다면 repr 함수가 사용됨
str: Kim
str: Lee
str: Lee
'''
