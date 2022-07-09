# Chapter03-1
# 컨테이너(Container) : 서로다른 자료형을 저장할 수 있음 [list, tuple, collections.deque],
# Flat : 한 개의 자료형 밖에 저장 안됨 [str,bytes,bytearray,array.array, memoryview]  => 속도가 컨테이너 보다 빠름
# 리스트 보다 array를 사용함으로서 속도를 증가시킴

# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 컨테이너와 flat형 모두 반복 가능

# 지능형 리스트(Comprehending Lists)
# Non Comprehending Lists
chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    # 유니코드 리스트
    # codes1[i] = ord(s) # 인덱스를 추가해서 값을 넣을 수 있음
    codes1.append(ord(s))

# Comprehending Lists
codes2 = [ord(s) for s in chars]

# 40번 이상의 숫자를 갖고오기 / 불필요한 코딩
# for s in chars:
#     if int(ord(s)) >= 40:
#         codes1.append(ord(s))

# Comprehending Lists + Map, Filter
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(filter(lambda x : x >40, map(ord, chars)))

codes4_1 = list(map(ord, chars))
print(codes4_1)

# 전체 출력
print('EX1-1 -', codes1)
print('EX1-2 -', codes2)
print('EX1-3 -', codes3)
print('EX1-4 -', codes4)
print('EX1-5 -', [chr(s) for s in codes1])
print('EX1-6 -', [chr(s) for s in codes2])
print('EX1-7 -', [chr(s) for s in codes3])
print('EX1-8 -', [chr(s) for s in codes4])

print()
print()

# Generator 생성 방법
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지X / 일괄생성하지 않음 -> 성능이 엄청 좋음)
tuple_g = (ord(s) for s in chars)  #값이 나오지 않고 대기상태 / 값이 나오게 하기 위해서는 next 함수 사용
tuple_l = [ord(s) for s in chars]
print(tuple_g)  # 하나의 값만 메모리에 올림
print(next(tuple_g)) # 33 값이 하나 나옴
print(next(tuple_g)) # 64 값이 하나 나옴

print(tuple_l)  # 모든 값을 메모리에 올림


# Array
array_g = array.array('I',  (ord(s) for s in chars))
print(array_g)
print(array_g.tolist()) # 리스트로 형 변환이 일어난다.

array_k = array.array('d', (ord(s) for s in chars))
print(array_k)
print(array_k.tolist())


print('EX2-1 -', type(tuple_g))
print('EX2-2 -', next(tuple_g))
print('EX2-3 -', type(array_g))
print('EX2-4 -', array_g.tolist())

print()
print()

# 제네레이터 예제
# 값이 나오지 않음
print('EX3-1 -', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))
print(['%s' %c + str(n) for c in 'A B C D'.split() for n in range(1,5)])

# 값이 나옴
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print('EX3-2 -', s)


print()
print()

# 리스트 주의 할 점
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

print('EX4-1 -', marks1)
print('EX4-2 -', marks2)

print()

# 값을 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('EX4-3 -', marks1)
print('EX4-4 -', marks2)

# EX4-3 - [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~']]
# EX4-4 - [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]  중간이 모두 X로 바뀜


# id값으로 증명
print('EX4-5 -', [id(i) for i in marks1])
print('EX4-6 -', [id(i) for i in marks2])

# EX4-5 - [4404491920, 4404491760, 4404491680] 객체가 서로 다름 / 리스트 컴프리핸서로 해야 서로 다른 객체가 생성 / 매우 중요
# EX4-6 - [4404491520, 4404491520, 4404491520] 객체가 서로 같음 / 밖에서 곱하면 모두 같음

# Tuple Advanced
# Packing 과 Unpacking
# 불변

# a 는 몫, b는 나머지
a, b = divmod(100,9)
print(a,b )
# 11 1


b, a = a, b

print('EX5-1 -', divmod(100, 9))
print('EX5-2 -', divmod(*(100, 9))) # 하나의 인자를 unpacking * 해서 사용
print('EX5-3 -', *(divmod(100, 9))) # 결과값이 언패킹되어서 나옴 / 잘 사용안함

print()

x, y, *rest = range(10)
print('EX5-4 -', x, y, rest)
x, y, *rest = range(2)  # rest는 []
print('EX5-5 -', x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print('EX5-6 -', x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]

# l[0] = 6 # 튜플은 불변이기때문에 에러 발생
# m[0] = 6

print('EX6-1 -', l, id(l))
print('EX6-2 -', m, id(m))

# 객체가 변경됨
l = l * 2
m = m * 2

print('EX6-3 -', l, id(l))
print('EX6-4 -', m, id(m))


# 리스트인 경우에는 객체가 변하지 않음
# 리스트는 자기 자신 안쪽에서 변경이 이뤄짐 ->  ID 는 변하지 않음
# 튜플은 객체가 변함 -> ID 값이 변함
l *= 2
m *= 2

print('EX6-5 -', l, id(l))
print('EX6-6 -', m, id(m))

print()
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func..

# sorted : 정렬 후 새로운 객체 반환 / 원본은 변경안됨
# sorted(대상) 오는 반면, 대상.sort() 형식으로 사용
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

test = sorted(f_list) # sorted는 반드시 다른 변수에 저장해야 한다. 반면에 sort는 바로 원본 자료가 바뀜
print(test)
print(f_list) # 원본은 그대로 있음

print('EX7-1 -', sorted(f_list))
print('EX7-2 -', sorted(f_list, reverse=True))
print('EX7-3 -', sorted(f_list, key=len))
print('EX7-4 -', sorted(f_list, key=lambda x: x[-1]))
print('EX7-5 -', sorted(f_list, key=lambda x: x[-1], reverse=True))
print()

print('EX7-6 -', f_list)

print()

# sort : 정렬 후 객체 직접 변경

# 반환 값 확인(None), 반환값이 None인 경우에는 객체 원본이 바로 바뀜을 뜻함
print('EX7-7 -', f_list.sort(), f_list)
print('EX7-8 -', f_list.sort(reverse=True), f_list)
print('EX7-9 -', f_list.sort(key=len), f_list)
print('EX7-10 -', f_list.sort(key=lambda x: x[-1]), f_list)
print('EX7-11 -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트의 거의 모든 연산 지원)