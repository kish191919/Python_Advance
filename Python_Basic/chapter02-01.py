# Chapter02-1
# 파이썬 심화
# 데이터 모델(Data Model)
# 참조 : https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 시퀀스 : 리스트, 집합
# 시퀀스에는 반복이 가능함 / '__iter__' 가 있음
a = [1,2,3,4]
print(dir(a))


# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id 함수 (주소값 반환),  type 합수 (데이터의 자료형 반환)-> value
a = 7
print(id(a), type(a), dir(a))
for i in dir(a):
    print(i)


# 일반적인 튜플 사용 (값을 불변함, 추가는 가능, 리스트보다 속도는 빠름)
# 두 점 사이의 거리
# 0번째 인댁스 x, 1번째 인덱스 y 등으로 표기해놔야함 -> 매우 불편하고 복잡함
# 그래서 라벨을 붙이고 싶어함
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

print('EX1-1 -', line_leng1)

# 아래와 같이 클래스로 하면 좋긴하지만 좀 heavy해 보임.
# 그래서 네임드 튜플이 필요함
# class a:
#     self.x
#     self.y


# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
# 네임드 튜플은 클래스 형태로 받아들여서 대문자로 주로 표기 / 객채로 인식
# Point = namedtuple('가짜로 사용할 이름/ 임으로 만듬', '사용할 것을 뛰어서 사용')
Point = namedtuple('Point', 'x y')

# 두 점 선언
# 클래스와 비슷하게 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

# 계산
line_leng2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

# 출력
print('EX1-2 -', line_leng2)
print('EX1-3 -', line_leng1 == line_leng2)


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point',['x','y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y') #두개의 단어로 이뤄질 경우에는 적합하지 않음 'south korea'
Point4 = namedtuple('Point', 'x y x class', rename=True)  # x가 중복으로 사용되고 class 예약어를 사용할 수 없음/ # rename Default=False

# 출력
print('EX2-1 -', Point1, Point2, Point3, Point4)
# 클래스 형태로 표기됨
# EX2-1 - <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'>

print()
print()

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40) # x 똑같은게 2개 있고 class 예약어가 있음

# 딕셔너리를 언팩킹하려면 **을 앞에사 붙임
# ** 사용안하면 temp_dict를 x로 인식
p5 = Point3(**temp_dict)

# 출력
print('EX2-2 -', p1, p2, p3, p4, p5)
# EX2-2 - Point(x=10, y=35) Point(x=20, y=40) Point(x=45, y=20) Point(x=10, y=20, _2=30, _3=40) Point(x=75, y=55)
# p4 의 중복된 x와 class 예약어는 자동으로 rename되어서 표기됨

# p4._2 또는 p4._3 으로 값을 갖고올수 있음
print('EX2-2 -', p1, p2, p3, p4._2, p5)
# EX2-2 - Point(x=10, y=35) Point(x=20, y=40) Point(x=45, y=20) 30 Point(x=75, y=55)

print()
print()

# 사용
print('EX3-1 -', p1[0] + p2[1]) # Index Error 주의 / 인덱스로도 접근 가능 / 튜플의 기능을 갖고 있음
print('EX3-2 -', p1.x + p2.y) # 굳이 인덱스로 사용안함 / 클래스 변수 접근 방식

# Unpacking
x, y = p3

print('EX3-3 -', x+y)

# Rename 테스트 / 만약 rename을 true 하지 않을 경우 에러발생
print('EX3-4 -', p4)

print()
print()

# 네임드 튜플 메소드
# 리스트는 반복, 시퀀스 특징 갖고 있음
temp = [52, 38]

# _make() : 리스트를 사용해서 새로운 객체 생성
# temp의 인수 갯수가 Point1 에 들어갈 인수의 갯수와 맞아야함
p4 = Point1._make(temp)

print('EX4-1 -', p4)

#_fields : 필드 네임 확인 / 네이드튜플 안에 무엇이 있는지 확인

print('EX4-2 -', p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
# 키값을 기준으로 정렬됨
# orderedDict를 다시 dictionary로 바꿔줌
print('EX4-3 -', p1._asdict(), p4._asdict())
print(dict(p1._asdict()))


# _replace() : 수정된 '새로운' 객체 반환
# 튜플은 불변이라서 replace를 사용하면 새로운 객채로 만들어짐
print('EX4-4 -', p2._replace(y=100))

print()
print()

# 실 사용 실습
# 학생 전체 그룹 생성
# 반20명 , 4개의 반-> (A,B,C,D) 번호 총 80명
# 이를 리스트로 만들어야함

# 네임드 튜플 선언 / 변수명과 namedtuple 안에 변수는 동일하게 하는게 관계
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print('EX5-1 -', len(students))
print('EX5-2 -', students)

# 4번째 학생의 반/번호
print('EX5-3 -', students[4].rank)
print('EX5-3 -', students[4].number)



# 가독성 안좋은 케이스
students2 = [Classes(rank, number)
                    for rank in 'A B C D'.split()
                        for number in [str(n)
                            for n in range(1,21)]]

print()
print()

print('EX6-1 -', len(students2))
print('EX6-2 -', students2)

print()
print()

# 출력
for s in students:
    print('EX7-1 -', s)