# Chapter03-2
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# print(__builtins__.__dict__)

# Dict 구조
print('EX1-1 -')
# builtins 함수들을 딕셔너리 형식으로 보여줌
# print(__builtins__.__dict__)

print()
print()

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))  # 값을 변경할수 없음
t2 = (10, 20, [30, 40, 50])  # 값 중에 리스트가 있어서 값을 변경하게 딤

print('EX1-2 -', hash(t1))  # 해시값을 나오게 함 / 불변형만 해시할 수 있음
# print('EX1-3 -', hash(t2))

# EX1-2 - 5737367089334957572


t2[2][0]  = 10
print(t2)  # t2의 값이 변경이 됨
# (10, 20, [10, 40, 50])

print()
print()

# 지능형 딕셔너리(Comprehending Dict)
import csv

# 외부 CSV TO List of tuple

with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
    temp = csv.reader(f)
    ## print(temp)
    ## <_csv.reader object at 0x101a01cd0>

    # Header Skip
    next(temp)  #('Name', 'Code')

    # 리스트 안의 튜플 형식으로 변환
    NA_CODES = [tuple(x) for x in temp]

print('EX2-1 -', )
print(NA_CODES)  # 리스트 안의 튜플

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}

print()
print()

print('EX2-2 -', )
print(n_code1)   # 튜플이 두개의 값으로 나눠서 country, code로 디셔너리 안에 입력됨

print()
print()

print('EX2-3 -', )
print(n_code2)

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print('EX3-1 -', new_dict1)
# EX3-1 - {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}


# # Use setdefault
# 동일한 키의 값들은 리스트로 추가해줌
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print('EX3-2 -', new_dict2)
# EX3-2 - {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}

print()
print()


# 사용자 정의 dict 상속(UserDict 가능)

class UserDict(dict):
    def __missing__(self, key):
        print('Called : __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print('Called : __getitem__')
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        print('Called : __contains__')
        return key in self.keys() or str(key) in self.keys()


user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one': 1, 'two': 2})
user_dict3 = UserDict([('one', 1), ('two', 2)])

# 출력
print('EX4-1 -', user_dict1, user_dict2, user_dict3)
print('EX4-2 -', user_dict2.get('two'))
print('EX4-3 -', 'one' in user_dict3)
# print('EX4-4 -', user_dict3['three'])
print('EX4-5 -', user_dict3.get('three'))
print('EX4-6 -', 'three' in user_dict3)

print()
print()

# immutable Dict

from types import MappingProxyType

d = {'key1': 'TEST1'}

# Read Only
d_frozen = MappingProxyType(d)

print('EX5-1 -', d, id(d))
print('EX5-2 -', d_frozen, id(d_frozen))
print('EX5-3 -', d is d_frozen, d == d_frozen)

# 수정 불가
# d_frozen['key2'] = 'TEST2'

d['key2'] = 'TEST2'

print('EX5-4 -', d)
#
print()
print()

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set()  # Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')

# 추가 불가
# s5.add('Melon')

print('EX6-1 -', s1, type(s1))
print('EX6-2 -', s2, type(s2))
print('EX6-3 -', s3, type(s3))
print('EX6-4 -', s4, type(s4))
print('EX6-5 -', s5, type(s5))

# 선언 최적화

from dis import dis

print('EX6-5 -')
print(dis('{10}'))

print('EX6-6 -')
print(dis('set([10])'))

print()
print()

# 지능형 집합(Comprehending Set)
# name 함수는 유니코드를 설명해줌
from unicodedata import name

print('EX7-1 -')

print({name(chr(i), '') for i in range(0, 256)})

print({chr(i) for i in range(0, 256)})