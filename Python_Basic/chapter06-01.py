# 흐름제어, 병행처리(Concurrency)
# 제네레이터, 반복형
# Generator

# 파이썬 반복형 종류
# for, collections, text file(open 해서 갖고오면 가능), List, Dict, Set, Tuple, unpacking, *args
# 공부할 것 : 반복형 객체 내부적으로 iter 함수 내용, 제네레이터 동작 원리, yield from

# 반복 가능한 이유? -> iter( ) 함수 호출하기 때문에 가능

t = 'ABCDEF'

# for 사용
for c in t:
    print('EX1-1 -', c)

print()

# while 사용

w = iter(t)
print(w)
# <str_iterator object at 0x1084ca250>

while True:
    try:
        print('EX1-2 -', next(w))
    except StopIteration as log:    # next 해서 데이터가 없을때 빠져나옴
        print(log)
        break

print()

from collections import abc   # 추상클래스

# 반복형 확인
print('EX1-3 -', hasattr(t, '__iter__'))   # hasattr : 어떠한 속성을 갖고 있는지 여부
print('EX1-4 -', isinstance(t, abc.Iterable))   # isinstance : t가 abc의 Iterable인지 확인   / dir 로도 확인 가능

print()
print()


# next 사용

class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]   # 첫번째 리스트
        except IndexError:
            # pass
            raise StopIteration('Stop! Stop!')
        self._idx += 1
        return word

    def __iter__(self):
        print('Called __iter__')
        return self

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitIter('Who says the nights are for sleeping')

print('EX2-1 -', wi)
print('EX2-2 -', next(wi))
print('EX2-3 -', next(wi))
print('EX2-4 -', next(wi))
print('EX2-5 -', next(wi))
print('EX2-6 -', next(wi))
print('EX2-7 -', next(wi))
print('EX2-8 -', next(wi))
# print('EX2-9 -', next(wi))

print()
print()


# Generator 패턴
# 1.지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가 될 경우 메모리 사용량 증가 -> 제네레이터 완화
# 2.단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3.딕셔너리, 리스트 한 번 호출 할 때 마다 하나의 값만 리턴 -> 아주 작은 메모리 양을 필요로 함

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word  # 제네레이터
        return

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wg = WordSplitGenerator('Who says the nights are for sleeping')

wt = iter(wg)  # next 가 없기때문에 iter 함수를 통해서 iterable 하게 바꿔져야함 -> next를 사용가능함

print('EX3-1 -', wt)
# print(wt[7])        # 인덱스는 안됨
print('EX3-2 -', next(wt))
print('EX3-3 -', next(wt))
print('EX3-4 -', next(wt))
print('EX3-5 -', next(wt))
print('EX3-6 -', next(wt))
print('EX3-7 -', next(wt))
print('EX3-8 -', next(wt))
# print('EX3-9 -', next(wt))

print()
print()


# Generator 예제1

def generator_ex1():
    print('start')
    yield 'AAA'
    print('continue')
    yield 'BBB'
    print('end')


temp = iter(generator_ex1())   # iter로 하지 않을 경우 "AAA" 만 나오게 됨

print('EX4-1 -', next(generator_ex1()))
print('EX4-2 -', next(generator_ex1()))
print('EX4-3 -', next(generator_ex1()))

print('EX4-1-1 -', next(temp))
print('EX4-2-2 -', next(temp))
# print('EX4-3-3 -', next(temp)) # 마지막은 없음

for v in generator_ex1():     # for 문에서 next 를 자동으로 해줌
    # pass
    print('EX4-3 -', v)

print()

# Generator 예제2

temp2 = [x * 3 for x in generator_ex1()]   # x는 yield로 넘어간 값임
temp3 = (x * 3 for x in generator_ex1())

print('EX5-1 -', temp2)
print('EX5-2 -', temp3)

for i in temp2:
    print('EX5-3 -', i)

print()
print()

for i in temp3:
    print('EX5-4 -', i)

print()
print()

# Generator 예제3(자주 사용하는 함수)

import itertools

gen1 = itertools.count(1, 2.5)  # 1에서 2.5를 더하고 next 하면 이후 2.5를 더해서 무한대로 계속 보내줌

print('EX6-1 -', next(gen1))
print('EX6-2 -', next(gen1))
print('EX6-3 -', next(gen1))
print('EX6-4 -', next(gen1))
# ... 무한

print()

# 조건
# 종료값을 원할때는 takewhile 을 사용함
gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))

for v in gen2:
    print('ex6-5 -', v)

print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print('EX6-6 -', v)

print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print('EX6-7 -', v)

print()

# 연결1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))

print('EX6-8 -', list(gen5))

# 연결2

gen6 = itertools.chain(enumerate('ABCDE'))

print('EX6-9 -', list(gen6))

# 개별
gen7 = itertools.product('ABCDE')

print('EX6-10 -', list(gen7))

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)

print('EX6-11 -', list(gen8))

# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')

# print('EX6-12 -', list(gen9))

for chr, group in gen9:
    print('EX6-12 -', chr, ' : ', list(group))

print()