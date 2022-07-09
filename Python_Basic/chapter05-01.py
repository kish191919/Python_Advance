# Chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrence

print('EX1-1 -')
print(dir.__name__)
print(dir())

# dir
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


# 얕은 복사
# id vs __eq__ (==) 증명
x = {'name': 'kim', 'age': 33, 'city': 'Seoul'}
y = x

print('EX2-1 -', id(x), id(y))
print('EX2-2 -', x == y)
print('EX2-3 -', x is y)
print('EX2-4 -', x, y)

# x 와 y 값 모두 class:10 이 입력이 됨 / 주의 바람
x['class'] = 10
print('EX2-5 -', x, y)
# EX2-5 - {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10} {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10}


print()
print()

z = {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10}

print('EX2-6 -', x, z)
print('EX2-7 -', x is z) # 값은 같으나 다른 객체
print('EX2-8 -', x is not z)
print('EX2-9 -', x == z) # 값이 같다

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__) 는 값 비교
# is 값으로 먼저 두개의 객체를 비교하고 이후 값을 비교함 (연산량이 많이 줄어듦)

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2))
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple2))

print()
print()

# Copy, Deepcopy(얕은 복사, 깊은 복사)

# Copy 얕은 복사
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1) #새로 만들어서 새 변수에 할당해서 새 객체를 만듬

print(tl3)   # [10, [100, 105], (5, 10, 15)]
print('EX4-1 -', tl1 == tl2)
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-4 -', tl1 is tl3)

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)   # 바뀜
print('EX4-6 -', tl2)   # 바뀜
print('EX4-7 -', tl3)  # 안바뀜


# EX4-5 - [10, [100], (5, 10, 15), 1000]
# EX4-6 - [10, [100], (5, 10, 15), 1000]
# EX4-7 - [10, [100], (5, 10, 15)]
print()

print(id(tl1[2]))      # 튜플 할당전 ID  :  4357450160
tl1[1] += [110, 120]
tl1[2] += (110, 120)

print('EX4-8 -', tl1)
print('EX4-9 -', tl2)  # 튜플 재 할당(객체 새로 생성)

# 튜플의 경우, 값이 추가되면서 새로 객체가 생성됨
# 리스트의 경우, 값이 같은 객체에 그대로 추가, 객체는 변함없음
# 보통 리스트 안에 튜플을 넣어서 사용을 않도록 함 -> 객체가 볌함에 따라서 데이터 소실 우려
print(id(tl1[2]))      # 튜플 할당후 ID   :  4357049424
print('EX4-10 -', tl3)



# 4424182192
# EX4-8 - [10, [100, 110, 120], (5, 10, 15, 110, 120), 1000]
# EX4-9 - [10, [100, 110, 120], (5, 10, 15, 110, 120), 1000]
# 4423781456
# EX4-10 - [10, [100, 110, 120], (5, 10, 15)]


print()
print()

# Deep Copy

# 장바구니
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX5-1 -', id(basket1), id(basket2), id(basket3))   # 모든 객체의 ID 값이 다 다름
print('EX5-2 -', id(basket1._products), id(basket2._products), id(basket3._products))  # 안에있는 객체는 basket1, basket2 이 동일

# EX5-1 - 4386474576 4386309136 4386248272
# EX5-2 - 4386238784 4386238784 4386221344

print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

# 객체복사는 가능한 deepcopy를 사용함
print('EX5-3 -', basket1._products)  # 객체 안의 객체가 basket1과 basket2가 동일함
print('EX5-4 -', basket2._products)
print('EX5-5 -', basket3._products)


# EX5-3 - ['Apple', 'Bag', 'TV', 'Water', 'Orange']
# EX5-4 - ['Apple', 'Bag', 'TV', 'Water', 'Orange']
# EX5-5 - ['Apple', 'Bag', 'TV', 'Snack', 'Water']

print()
print()

# 함수 매개변수 전달 사용법

def mul(x, y):
    x += y
    # x = x + y  동일한 값
    return x

x = 10
y = 5

print('EX6-1 -', mul(x, y), x, y)
# EX6-1 - 15 10 5
print()


a = [10, 100]
b = [5, 10]

print('EX6-2 -', mul(a, b), a, b) # 가변형 a -> 원본 데이터 변경
# EX6-2 - [10, 100, 5, 10] [10, 100, 5, 10] [5, 10]


c = (10, 100)
d = (5, 10)

print('EX6-2 -', mul(c, d), c, d) # 불변형 c -> 원본 데이터 변경 안됨
# EX6-2 - (10, 100, 5, 10) (10, 100) (5, 10)




# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple : 사본 생성 X -> 참조 반환
# frozenset 을 다른 변수에 담아놔도 frozenset 자체가 변하지 않기때문에 변경이 일어나지 않음


tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)  # id 번호가 안변함
tt3 = tt1[:]      # id 번호가 안변함  # 모든 ID 값이 동일함

print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 -', tt3 is tt1, id(tt3), id(tt1))

# EX7-1 - True 4444322896 4444322896
# EX7-2 - True 4444322896 4444322896


tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))