# Chapter04-1
# 파이썬 일급 함수 특징
# 1.런타임 초기화 가능  / 실행시에 초기화 가능
# 2.변수 등에 할당 가능
# 3.함수 인수 전달 가능  / sorted(keys=lens)
# 4.함수 결과로 반환 가능  / return funcs 함수


# 함수 객체 예제
# factorial(5) : 5 * 4 * 3 * 2 * 1
def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass


print('EX1-1 -', factorial(5))
print('EX1-2 -', factorial.__doc__)
print('EX1-3 -', type(factorial), type(A))

# 함수와 클래스의 차이점 확인 / 리스트는 빼기를 할 수 없기때문에 set을 이용
print('EX1-4 -', set(sorted(dir(factorial))) - set(sorted(dir(A))))
print('EX1-5 -', factorial.__name__)  # 함수의 이름을 나타냄
print('EX1-5 -', factorial.__code__)  # 파일이 어디에 있는지 위치확인

print()
print()

# 변수 할당
# var_func = factorial() / ()부분을 삭제해야 할당이 됨
var_func = factorial

print('EX2-1 -', var_func)
print('EX2-2 -', var_func(10))
print('EX2-3 -', map(var_func, range(1,11)))
print('EX2-4 -', list(map(var_func, range(1,6))))

# EX2-1 - <function factorial at 0x10731c5f0>
# EX2-2 - 3628800
# EX2-3 - <map object at 0x107316c10>
# EX2-4 - [1, 2, 6, 24, 120]

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce 등

print('EX3-1 -', list(map(var_func, filter(lambda x: x % 2, range(1,6)))))  # 홀수만 실행 (1,3,5)
print('EX3-2 -', [var_func(i) for i in range(1,6) if i % 2])

# reduce 함수
from functools import reduce
from operator import add

print('EX3-3 -', reduce(add, range(1,11))) # 누적 1+2+3+4+5+...10 / 이전의 함수값을 사용해서 누적시킴
print('Ex3-4 -', sum(range(1,11)))


# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 사용
# 일반 함수 형태로 리팩토링 권장

print('EX3-4 -', reduce(lambda x, t: x + t, range(1,11)))
print()
print()


# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# def, built-in functions, 내장 메소드, class, method...

# 호출 가능 확인 / 함수여부 확인  str(), list(), var_func()... 함수들을 callable이라고 함
print('EX4-1 -', callable(str), callable(list), callable(var_func), callable(3.14) )

import random

# 로또 추첨 클래스 선언
class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1,46)]

    def pick(self):
        print(random.shuffle(self._balls))   # 원래 데이터 자체가 바뀜으로 반환 값은 None
        print(self._balls)                   # 바뀐 데이터 확인
        return sorted([random.choice(self._balls) for n in range(6)])

    def __call__(self):     # 매우 중요한 개념
        return self.pick()


# 객체 생성
game = LottoGame()
#
# 게임 실행
print('EX4-2 -', game.pick())
print('EX4-3 -', game())  # __call__이 작동하여 self.pick() 작동됨  / filter, map 등의 함수의 인자로 넘길수 있음

# 객체 직접 호출
print('EX4-4 -', callable(game))    # game() 이 되므로 callable 하다고 함
print('EX4-5 -', game.pick())


print()
print()


# 다양한 매개변수 입력(*args, **kwargs)
def agrs_test(name, *contents, point=None, **attrs):
    return '<agrs_test> -> ({}) ({}) ({}) ({})'.format(name, contents, point, attrs)


print('EX5-1 -', agrs_test('test1'))
print('EX5-2 -', agrs_test('test1', 'test2'))
print('EX5-3 -', agrs_test('test1', 'test2', 'test3'))
print('EX5-4 -', agrs_test('test1', 'test2', 'test3', id='admin'))
print('EX5-4 -', agrs_test('test1', 'test2', 'test3', id='admin', point=7))
print('EX5-4 -', agrs_test('test1', 'test2', 'test3', id='admin', password='1234', point=7))


# EX5-1 - <agrs_test> -> (test1) (()) (None) ({})                  *args : 튜플로 받음  / **kwargs : 딕셔너리로 받음
# EX5-2 - <agrs_test> -> (test1) (('test2',)) (None) ({})          튜플하나는 쉼표가 있음  (('test2',))
# EX5-3 - <agrs_test> -> (test1) (('test2', 'test3')) (None) ({})
# EX5-4 - <agrs_test> -> (test1) (('test2', 'test3')) (None) ({'id': 'admin'})
# EX5-4 - <agrs_test> -> (test1) (('test2', 'test3')) (7) ({'id': 'admin'})
# EX5-4 - <agrs_test> -> (test1) (('test2', 'test3')) (7) ({'id': 'admin', 'password': '1234'})


print()
print()

# 함수 Signatures

from inspect import signature

sg = signature(agrs_test)

print('EX6-1 -', sg)  #파라미터들을 볼수 있음
print('EX6-2 -', sg.parameters)

print()

# 모든 정보 출력
for name, param in sg.parameters.items():               # 매개변수의 상세한 파라미터 보여줌
    print('EX6-3 -', name, param.kind, param.default)

print()
print()

# partial 사용법 : 인수 고정 -> 주로 특정 인수 고정 후 콜백 함수에 사용
# 하나 이상의 인수가 이미 할당된 (채워진) 함수의 새 버전 반환
# 함수의 새 객체 타입은 이전 함수의 자체를 기술하고 있음
from operator import mul
from functools import partial

print('EX7-1 -', mul(10,10))

# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)

print('EX7-2 -', five(10))  # 인자 1개는 고정시킴
print('EX7-3 -', six())     # 인자를 이미 2개를 다 사용함
print('EX7-4 -', [five(i) for i in range(1,11)])
print('EX7-5 -', list(map(five, range(1,11))))