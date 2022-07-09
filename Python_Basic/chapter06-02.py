# 흐름제어, 병행처리(Concurrency)
# yield : 메인루틴 <-> 서브 루틴
# 코루틴 제어, 코루틴 상태, 양방향 값 전송
# yield from

# 서브루틴 : 메인루틴에서 -> 리턴에 의해 호출 부분으로 돌아와 다시 프로세스
# 코루틴 : 루틴 실행 중 멈춤 가능 -> 특정 위치로 돌아갔다가 -> 다시 원래 위치로 돌아와 수행 가능 -> 동시성 프로그래밍 가능
# 코루틴 : 코루틴 스케쥴링 오버헤드 매우 적다.
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가

# 코루틴 예제1

def coroutine1():
    print('>>> coroutine started.')
    i = yield  # 메인루틴에서 리턴을 받음 // i 값을 받아야 실행이 됨 // 코루틴은 비동기화 되기때문에 동시성이 가  // yield 'value'  일 경우에는 값을 반환 /
    print('>>> coroutine received : {}'.format(i))

# 제네레이터 선언  / yield문에서 멈춤 next 나와야 다음으로 실행

c1 = coroutine1()
print('EX1-1 -', c1, type(c1))
# EX1-1 - <generator object coroutine1 at 0x10f3c9ed0> <class 'generator'>  재너레이터가 있음

# yield 실행 전까지 진행
next(c1)
# >>> coroutine started. 까지 실행 -> None 값을 전달


# 기본으로 None 전달
# next(c1)

# 값 전송함으로서 다시 함수가 시작됨. / 다른 코로틴에게 보내서 실행 가능함
# c1.send(100)
# >>> coroutine received : 100


# 잘못된 사용

# c2 = coroutine1()
# next(c2)  / 실행하지 않으면 아래 명령문에 에러 발생
# c2.send(100) # 예외 발생  / 바로위에 next(c2)를 실행하여 yield까지 내려와야함

# 코루틴 예제2
# GEN_CREATED : 처음 대기 상태  / Next를 호출하기 전
# GEN_RUNNING : 실행 상태   / Next를 호출
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


c3 = coroutine2(10)

from inspect import getgeneratorstate  # 코루틴 상태값을 볼쓰 있음

print('EX1-2 -', getgeneratorstate(c3))

print(next(c3))  # 코루틴을 할때 항상 next를 사용함 그러나 데코래이터를 사용하여 이를 해결

print('EX1-3 -', getgeneratorstate(c3))

print(c3.send(15))

# print(c3.send(20)) # 예외

print()
print()

# 데코레이터 패턴

from functools import wraps

def coroutine(func):
    '''Decorator run until yield'''
    @wraps(func)
    def primer(*args, **kwargs):  # 모든 인수를 받음
        gen = func(*args, **kwargs)   # function 실행
        next(gen)
        return gen
    return primer

@coroutine
def sumer():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term


su = sumer()

print('EX2-1 -', su.send(100))  # 데코레이터에서 next가 실행되므로 따로 sumer에 next함수를 붙일 필요가 없음
print('EX2-2 -', su.send(40))
print('EX2-3 -', su.send(60))


# 코루틴 예제3(예외처리)

class SampleException(Exception):
    '''설명에 사용할 예외 유형'''


def coroutine_except():
    print('>> coroutine stated.')
    try:
        while True:
            try:
                x = yield
            except SampleException:
                print('-> SampleException handled. Continuing..')
            else:
                print('-> coroutine received : {}'.format(x))
    finally:
        print('-> coroutine ending')


exe_co = coroutine_except()

print('EX3-1 -', next(exe_co))
print('EX3-2 -', exe_co.send(10))
print('EX3-3 -', exe_co.send(100))
print('EX3-4 -', exe_co.throw(SampleException))    # 에러를 던져도 코루틴이 계속 작동
print('EX3-5 -', exe_co.send(1000))
print('EX3-6 -', exe_co.close()) # GEN_CLOSED

print()
print()

# 코루틴 예제4(return)

def averager_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total / cnt
    return 'Average : {}'.format(avg)

avger2 =averager_re()

next(avger2)

avger2.send(10)
avger2.send(30)
avger2.send(50)


try:
    avger2.send(None)
except StopIteration as e:
    print('EX4-1 -', e.value)


# 코루틴 예제5(yeild from)
# StopIteration 자동 처리(3.7 -> await)
# 중첩 코루틴 처리

def gen1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y

t1 = gen1()

print('EX5-1 -', next(t1))
print('EX5-2 -', next(t1))
print('EX5-3 -', next(t1))
print('EX5-4 -', next(t1))
print('EX5-5 -', next(t1))
# print('EX5-6 -', next(t1))

t2 = gen1()

print('EX5-7 -', list(t2))

print()
print()

def gen2():
    yield from 'AB'
    yield from range(1,4)



t3 = gen2()

print('EX6-1 -', next(t3))
print('EX6-2 -', next(t3))
print('EX6-3 -', next(t3))
print('EX6-4 -', next(t3))
print('EX6-5 -', next(t3))
# print('EX6-6 -', next(t3))

t4 = gen2()

print('EX6-7 -', list(t4))


print()
print()

def gen3_sub():
    print('Sub coroutine.')
    x = yield 10
    print('Recv : ', str(x))
    x = yield 100
    print('Recv : ', str(x))

def gen4_main():
    yield from gen3_sub()

t5 = gen4_main()

print('EX7-1 -', next(t5))
print('EX7-2 -', t5.send(7))
print('EX7-2 -', t5.send(77))