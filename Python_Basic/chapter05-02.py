# Chapter05-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Special Method, Class ABC (추상클래스)

class VectorP(object):
    # private 선언
    def __init__(self, x, y):

        self._x = float(x)
        if y < 30:
            raise ValueError('y below 30 not possible')
        self._y = float(y)

v = VectorP(20,40)

print(v._x, v._y)
v._y = 'dfskdjfks'  # _y를 30 이하의 숫자가 아닌 전현 다른 인풋을 직접 넣을 수 있음.

print(v._x, v._y)
# 20.0 dfskdjfks


# class 선언
class VectorP(object):
    # private 선언
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))  # Generator

    @property   # getter 먼저 먼들고 이후에 setter를 만듬
    def x(self):
        return self.__x

    @x.setter
    def x(self, v):
        self.__x = v

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, v):
        if v < -273:
            raise ValueError("Temperature below -273 is not possible")
        self.__y = v


# 객체 선언
v5 = VectorP(20, -340)

# print('EX1-2 -', v5.__x, v5.__y)   # 아래 밑줄이 2개이면 직접 접근이 불가함. 밑줄 한개이거나 없어야 접근 가능

print('EX1-3 -', dir(v5), v5.__dict__)
print('EX1-4 -', v5.x, v5.y)  # 타 언어와 달리 근본적인 해결책 X, 파이썬 개발자 간의 암묵적 약속

# Iter 확인
for v in v5:
    print('EX1-5 -', v)

print()
print()


# __slot__
# 파이선 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용(공간) 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 set 형태를 사용

# 성능 비교 (클래스 2개 선언)
class TestA(object):
    __slots__ = ('a',)  #튜플 형태로 a라는 속성만 있음 /  추가할 일이 있으면 여기에 추가시킴


class TestB(object):
    pass


use_slot = TestA()
no_slot = TestB()

print('EX2-1 -', use_slot)
# print('EX2-2 -', use_slot.__dict__)   # 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 set 형태를 사용되므로 검색이 안됨
print('EX2-3 -', no_slot)
print('EX2-4 -', no_slot.__dict__)

use_slot.a = 10
# use_slot.b = 10


# 메모리 사용량 비교
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'test'
        del obj.a

    return repeat_inner


# print('EX3-1 -', min(timeit.repeat(repeat_outer(use_slot), number=1000)))  # 함수를 반복하면서 시간을 측정
# print('EX3-2 -', min(timeit.repeat(repeat_outer(no_slot), number=1000)))

print()
print()


# 객체 슬라이싱
class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]

    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]


s = ObjectS()

# print('EX3-1 -', s.__dict__)
print('EX3-2 -', len(s._numbers))    # __len__ 없어도 실행가능
print('EX3-3 -', len(s))             # __len__ 없으면 오류발생
print('EX3-4 -', s[1:10])            # 클래스인데 리스트처럼 사용가능
print('EX3-5 -', s[-1])
print('EX3-6 -', s[::10])

print()
print()

# 파이썬 추상클래스
# 참고 : https://docs.python.org/3/library/collections.abc.html
# 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것
# 자체적으로 개체 생성 불가
# 상속을 통해서 자식 클래스에서 인스턴스를 생성해야함
# 폰 -> 걸다, 끊다, 배터리충전 -> 갤럭시 s3, 갤럭시 k3..


from collections.abc import Sequence

# Sequence 상속 받지 않았지만, 자동으로 __iter__, __contains__ 기능 작동
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜
class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]  # range(1, 50, 2)


i1 = IterTestA()

print('EX4-1 -', i1[4])
print('EX4-2 -', i1[4:10])  # [idx] 제거 후
print('EX4-3 -', 3 in i1[1:10])
print('EX4-4 -', [i for i in i1[:]])

print()
print()


# Sequence 상속
# 요구사항인 추상메소드 모두 구현해야 동작
# 만약 phone 이라 한다면 전화 걸다, 끝다, 충전하다 등을 모두 구현해야함
class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]  # range(1, 50, 2)

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])


i2 = IterTestB()

print('EX4-5 -', i2[4])
print('EX4-6 -', len(i2[:]))
print('EX4-7 -', len(i2[1:6]))

print()
print()

# abc 활용 예제 / 추상 클래스
import abc

class RandomMachine(abc.ABC):  # metaclass=abc.ABCMeta (3.4 이하 버전)
    # __metaclass__ = abc.ABCMeta

    # 추상 메소드
    @abc.abstractmethod
    def load(self, iterobj):
        '''iterable 항목 추가'''

    # 추상 메소드
    @abc.abstractmethod          # 데코레이터가 있는 부분은 반드시 자식클레스에서 구현해야함
    def pick(self, iterobj):
        '''무작위 항목 뽑기'''

    def inspect(self):
        print("부모클래스 실행")
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        return tuple(sorted(items))


import random
class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()  # 시스템의 타임스템프를 이용해서 보다 다양한 랜덤이 가능
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crane Box.')

    def __call__(self):
        return self.pick()

    # 메소드 오버라이드
    def inspect(self):
        print('Override Test---')


# 서브 클래스 확인
print('EX5-1 -', issubclass(RandomMachine, CraneMachine))  # 자식인지 여부를 확인   issubclass(자식, 부모)
print('EX5-2 -', issubclass(CraneMachine, RandomMachine))
# 상속 구조 확인
print('EX5-3 -', CraneMachine.__mro__)   # 상속구조 확인

cm = CraneMachine(range(1, 100))  # 추상메소드 구현 안하면 에러

print('EX5-4 -', cm._items)
print('EX5-5- ', cm.pick())
print('EX5-6- ', cm())          # Callable 되어는지 확인
print('EX5-7- ', cm.inspect())  # 자식이 없으면 부모 메소드가 실행이 됨