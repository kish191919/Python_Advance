class Student():
    """
    Student Class
    Author : Danny
    Date : 2022.07.04
    """

    # 클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None ):
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        # 클래스.클래스 변수를 사용해서 접근
        Student.student_count +=1

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
        return 'repr {}'.format(self._name)

    def detail_info(self):
        print("Current ID : {}".format(id(self)))  # Id 값, 레퍼런스 값
        print('Student Detail Info: {} {} {}'.format(self._name, self._email, self._details))

    # 지우기 / 이런식으로 잘 쓰지 않음
    def __del__(self):
        Student.student_count -= 1


# Self 의미
student1 = Student('Cho', 2, 3, {'gender':'Male', 'score1':65, 'score2':44})
student2 = Student('Chang', 4, 1, {'gender':'Female', 'score1':85, 'score2':74}, 'kish1919@gmail.com')

# 값이 같아도 id값이 다르다.
# id값이 같다면 값이 같다
print(id(student1))
print(id(student2))

print(id(student1._name == student2._name)) # == 실제 값을 확인함
print(student1 is student2)                 # is 는 id 값을 비교

a =  'ABC'
b = a

print(a is b)  # reference 를 비교
print(a == b)  # 값을 비교

print()
print()

# dir & __dict__ 확인
# 클래스의 속성값 볼때는 dict를 사용
# dir : 파이썬 내부 속성값 모두 표기 / 해당 인스턴스의 값은 보여주지 않음
print(dir(student1))
print(dir(student2))

print()
print()
# __dict__ : 해당 인스턴스의 값도 보여줌
print(student1.__dict__)
print(student2.__dict__)


# Docstring
# 누가 만들었는지 바로 확인 가능
print(Student.__doc__)
print()

# 실행
student1.detail_info()
student2.detail_info()

# 에러
# self 가 없어서 에러발생
# missing 1 required positional argument: 'self'
# Student.detail_info()

# self 부분에 인스턴스를 넣어주면 직접 접근이 가능
Student.detail_info(student1)

# 비교
# 클래스를 알려줌
# <class '__main__.Student'> <class '__main__.Student'>
print(student1.__class__, student2.__class__)

# 원형 클래스의 id를 나타냄으로 둘이 같음
print(id(student1.__class__) == id(student2.__class__))

print()

# 인스턴스 변수
# 직접 접근 (pep 문법적으로 권장하지 않음)
# 직접적으로 접근시 바로 값을 변하기 때문에 권장하지 않음
student1._name = "haha"
print(student1._name)


print()
print()

# 클래스 변수
# 접근
print(student1.student_count)
print(student2.student_count)
print(Student.student_count)

print()
print()

# 공유 확인
print(Student.__dict__)

# 인스턴스에는 클래스 변수는 없음
print(student1.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 인스턴스 검색후 -> 상위( 클래스 변수, 부모 클래스 변수 확인 후 출력)

print()

del student2
print(student1.student_count)