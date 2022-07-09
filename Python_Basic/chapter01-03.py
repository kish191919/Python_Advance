# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드
# 기본 인스턴스 메소드

class Student(object):
    '''
    Student Class
    Author : Danny
    Date : 2022.07.04
    Description :  Class, Static, Instance Method
    '''

    # Class Variable
    tuition_per = 1

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa



    # Instance Method
    # self를 통해서 인스턴스의 속성값에 접근가능
    def full_name(self):
        return '{},{}'.format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return 'Student Detail Info: {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._gpa)

    def get_fee(self):
        return 'Before Tuition -> ID : {}, fee : {}'.format(self._id, self._tuition)

    def get_fee_culc(self):
        return 'After tuition -> ID : {}, fee : {}'.format(self._id, self._tuition * Student.tuition_per)

    def __str__(self):
        return 'Student Info -> name : {}, grade : {}, email: {}'.format(self.full_name(), self._grade, self._email)

    # Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1 :
            print("Please Enter 1 or more")
            return
        # cls는 Student 와 동일함
        # 클래스 변수를 업데이트 해줌
        cls.tuition_per = per
        print("성공! 인상되었습니다.")

    # construct 메소드를 만드는 것을 선호함
    # 인스턴스가 만들어진다는 것을 명시적으로 표시가능
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)

    # Static Method
    # self, cls 도 받을필요가 없음
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return '{} is a scholarship recipient'.format(inst._last_name)
        return 'Sorry. not a scholarship recipient'




# 학생 인스턴스
student_1 = Student(1, 'Kim', 'Sarang', 'student1@naver.com', '1', 400, 3.5)
student_2 = Student(2, 'Lee', 'Myungho', 'student2@naver.com', '1', 500, 4.3)

# # 기본정보
# print(student_1)
# print(student_2)
# print()
#
# print(student_1.__dict__)
# print(student_2.__dict__)
#
# print(dir(student_1))
# print(dir(student_2))
# print()
#
# # 전체정보
# print(student_1.detail_info())
# print(student_2.detail_info())
# print()

# 학비 정보
print(student_1.get_fee())
print(student_2.get_fee())
print()

# 학비 인상(클래스 메소드 미사용 X)
# 직접 고치는 것은 권장하지 않음
# 캡슐화가 되어 보호되어야함
Student.tuition_per = 1.5

# 학비 인상(클래스 메소드 사용 O)
Student.raise_fee(1.2)

# 학비 인상
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())
print()


# 클래스 메소드 인스턴스 생성 실습
student_3 = Student.student_const(3, 'Park', 'Minji', 'student3@gmail.com', '3', 550, 4.5)
student_4 = Student.student_const(4, 'Cho', 'Sunghwan', 'student4@gmail.com', '4', 600, 2.5)

print(student_3.detail_info())
print(student_4.detail_info())

# 학생 학비 변경 확인
# construct에 이미 오른 값이 반영되어있음
# 그러기 때문에 인스턴스를 만들때, 학비가 오른 값과 오르기 전 값을 혼용하여 사용 가능함
print(student_3._tuition)
print(student_4._tuition)


# 장학금 혜택 여부 (스테이틱 메소드 미사용 X)
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return '{} is a scholarship recipient'.format(inst._last_name)
    return 'Sorry. not a scholarship recipient'

print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

print()
# 장학금 혜택 여부 (스테이틱 메소드 사용 O)
# 클래스를 이용
print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))
print()

# 인스턴스 이용 (자신을 인수로 넣어줌)
print(student_1.is_scholarship_st(student_1))
print(student_2.is_scholarship_st(student_2))
print(student_3.is_scholarship_st(student_3))
print(student_4.is_scholarship_st(student_4))