# Chapter04-2
# 파이썬 심화
# 일급 함수(일급 객체)
# Decorator & Closure
# 파이썬 변수 범위(global)

# 예제1
def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(5)
# 에러 : b is not defined


# 예제2
b = 10 # 전역영역

def func_v2(a):
    print(a)
    print(b)


func_v2(5)

# 예제3
b = 10

def func_v3(a):
    # global b
    print(a)
    print(b)  # b가 지역변수 안에 있는 것은 확인되었지만, 아직 값이 할당받기 전이기 때문에 에러가 발생
    b = 20    # 지역변수 우선

# func_v3(5)

# 증명과정
from dis import dis

print('EX1-1 -')
print(dis(func_v3))

print()
print()

# Closure(클로저)
# 반환되는 내부 함수에 대해서 선언된 연결을 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 적근이 가능함
# 클로저를 안쓰면 클래스로 만들어서 사용해도 됨
a = 10

print('EX2-1 -', a + 10)   # 20
print('EX2-2 -', a + 100)  # 110

# 결과를 누적 할 수 없을까?
print('EX2-3 -', sum(range(1, 51)))    # sum 함수는 값을 누적하여 합해줌
print('EX2-3 -', sum(range(51, 101)))

print()
print()


# 클래스 이용해서 인수를 누적시키기
class Averager():
    def __init__(self):
        self._series = []  # 리스트 선언

    def __call__(self, v):   # 객체를 직접 호출 가능
        self._series.append(v)  # 인수가 리스트에 계속 추가가 됨
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# 인스턴스 생성

avg_cls = Averager()

# 누적 확인
print('EX3-1 -', avg_cls(15))
print('EX3-2 -', avg_cls(35))
print('EX3-3 -', avg_cls(40))

print()
print()


# 클로저(Closure) 사용
# 전역변수 사용 감소
# 디자인 패턴 적용

def closure_avg1():
    # Free variable
    # 변수의 은닉화 가능
    # 이 부분은 계속 메모리에 담기때문에 자주 사용하게되면 리소스 소모가 일어남
    series = []

    # 클로저 영역
    def averager(v):
        # series = [] # Check
        series.append(v)
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager


avg_closure1 = closure_avg1()

# 함수가 끝나도 값은 계속 남아있음
print('EX4-1 -', avg_closure1(15))
print('EX4-2 -', avg_closure1(35))
print('EX4-3 -', avg_closure1(40))

print()
print()

# function inspection
print('EX5-1 -', dir(avg_closure1))
print()
print('EX5-2 -', dir(avg_closure1.__code__))  # co_freevars =  Free variable
print()
print('EX5-3 -', avg_closure1.__code__.co_freevars)   # series 물고 다님 / 튜플형태로 저장됨
print()
print('EX5-4 -', dir(avg_closure1.__closure__[0]))
print()
print('EX5-4 -', avg_closure1.__closure__[0].cell_contents)   # 메직 매소드가 있음

print()
print()


# 잘못된 클로저 사용 예
def closure_avg2():
    # Free variable
    cnt = 0
    total = 0

    # 클로저 영역
    def averager(v):
        # series = [] # Check
        cnt += 1  # cnt = cnt + 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_avg2()
# print('EX5-1 -', avg_closure2(15)) # 예외


# Nonlocal 사용 -> Free variable 변환
def closure_avg3():
    # Free variable
    cnt = 0
    total = 0

    # 클로저 영역
    def averager(v):
        nonlocal cnt, total  # 변수 cnt, total이 초기화가 안되서 에러발생 / nonlocal을 이용함으로서 위에 있는 변수들을 사용하겠다고 선언
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_avg3()

print('EX6-1 -', avg_closure3(15))
print('EX6-2 -', avg_closure3(35))
print('EX6-3 -', avg_closure3(40))

print()
print()

# 데코레이터 실습
# 1. 중복 제거, 코드 간결
# 2. 클로저 보다 문법 간결
# 3. 조합해서 사용 용이

# 단점
# 1. 디버깅 어려움
# 2. 에러의 모호함
# 3. 에러 발생지점 추적 어려움 (파이참은 이부분에서는 아주 잘되어있음)


# 항상 함수의 수행시간을 집어넣고 싶을때, 데코레이트 사용
import time

def perf_clock(func):               # 내가 실행할 함수 (func)을 받음
    def perf_clocked(*args):        # 튜플 형식으로 받음
        # 시작 시간
        st = time.perf_counter()    #  시작시간
        result = func(*args)        # 내가 실행할 함수
        # 종료 시간
        et = time.perf_counter() - st     # 실행한 시간
        # 함수명
        name = func.__name__               # 내가 실행한 함수의 이름
        # 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)     # 리스트 형식으로 인수들을 나타냄
        # 출력
        print('Result : [%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result

    return perf_clocked


@perf_clock
def time_func(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


@perf_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n - 1)


# 데코레이터 미사용
non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

print('EX7-1 -', non_deco1, non_deco1.__code__.co_freevars)
print('EX7-2 -', non_deco2, non_deco2.__code__.co_freevars)
print('EX7-3 -', non_deco3, non_deco3.__code__.co_freevars)

print('*' * 40, 'Called Non Deco -> time_func')
print('EX7-4 -')
non_deco1(0.5)
print('*' * 40, 'Called Non Deco -> sum_func')
print('EX7-5 -')
non_deco2(10, 15, 25, 30, 35)
print('*' * 40, 'Called Non Deco -> fact_func')
print('EX7-6 -')
non_deco3(10)

print()
print()

# 데코레이터 사용
# @functools.lru_cache() -> 추가 학습 권장

print('*' * 40, 'Called Deco -> time_func')
print('EX8-1 -')
time_func(0.5)
print('*' * 40, 'Called Deco -> sum_func')
print('EX8-2 -')
sum_func(10, 15, 25, 30, 35)
print('*' * 40, 'Called Deco -> fact_func')
print('EX8-3 -')
fact_func(10)