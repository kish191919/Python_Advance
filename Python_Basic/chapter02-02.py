# Chapter02-2
# 파이썬 심화
# Special Method(Magic Method)
# 참조1 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 참조2 : https://www.tutorialsteacher.com/python/magic-methods-in-python

# 매직메소드 기초 설명
#

# 기본형
# 모든 객체는 클래스로 되어있음
print(int)
# <class 'int'>

# 모든 속성 및 메소드 출력
print(dir(int))
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__'..] 등이 모두 매직매소드라고 함

print()
print()

n = 100

# 사용
print('EX1-1 -', n + 200)
print('EX1-2 -', n.__add__(200))  # + 가 자동으로 __add__으로 치환됨
print('EX1-3 -', n.__doc__)
print('EX1-4 -', n.__bool__(), bool(n))
print('EX1-5 - ', n * 100, n.__mul__(100))

print()
print()


# 클래스 예제1
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):  # 매직메소드를 오버라이딩해서 사용하면 보기 좋다
        return 'Student Class Info : {} , {}'.format(self._name, self._height)

    def __ge__(self, x):
        print('Called >> __ge__ Method.')
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called >> __sub__ Method.')
        return self._height - x._height


# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)

# 에러발생
# + (add) 가 클래스에서 정의되어 있지 않음
# print(s1 + s2)

print(s1._height > s2._height)
print(s1 >= s2) # 에러가 없음
# print(s1 > s2)  # > 은 클래서에서 정의하지 않음

print(s1 <= s2) # 에러 발생
# print(s1 < s2) # 에러 발생,  < 은 클래서에서 정의하지 않음


# 매직메소드 출력
print('EX2-1 -', s1 >= s2)
print('EX2-2 -', s1 <= s2)
print('EX2-3 -', s1 - s2)
print('EX2-4 -', s2 - s1)
print('EX2-5 - ', s1)
print('EX2-6 - ', s2)

print()
print()


# 클래스 예제2

class Vector(object):
    # *args : 튜플로 인자를 받아서 언팩킹함
    def __init__(self, *args):
        '''Create a vector, example : v = Vector(1,2)'''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args  #args는 튜플

    def __repr__(self):
        '''Returns the vector infomations'''
        return 'Vector(%r, %r)' % (self._x, self._y)  # %r 대신에 %f가 들어와도 됨

    def __add__(self, other):  # 두번째 백터를 other 인스턴스로 정의
        '''Returns the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):  # 벡터에 y 정수를 곱하는 것
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))  # x 와 y 값중 큰값이 0보다 클경우에는 true가 나옴


# Vector 인스턴스 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

# 매직메소드 출력
print('EX3-1 -', Vector.__init__.__doc__)  # init에 있는 docstring 을 나타냄
# EX3-1 - Create a vector, example : v = Vector(1,2)

print(v1, v2, v3)
# Vector(3, 5) Vector(15, 20) Vector(0, 0)

print('EX3-2 -', Vector.__repr__.__doc__)
print('EX3-3 -', Vector.__add__.__doc__)
print('EX3-4 -', v1, v2, v3)
print('EX3-5 -', v1 + v2)
print('EX3-6 -', v1 * 4)
print('EX3-7 -', v2 * 10)
print('EX3-8 -', bool(v1), bool(v2))
print('EX3-9 -', bool(v3))    # 0이기때문에 false를 반환

print()
print()

# 참고 : 파이썬 바이트 코드 실행
import dis

dis.dis(v2.__add__)