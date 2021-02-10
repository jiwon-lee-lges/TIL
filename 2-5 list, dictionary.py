# 불변 인자
a = [1, 2, 3, 4, 5]
b = a
a[2] = 4
a
b

# 가변 인자
a = 2
b = a
a = 4
a
b

# C++
# int a = 10;
# int &b = a;
# b = 7;
# std::cout << a << std::endl; # 공간에 id 할당

# is와 ==
if a is None:
    pass # None은 ==로 비교 불가능

a = [1, 2, 3]
a == a # True # ==는 값을 비교

a == list(a) #  True

a is a # id를 비교 # True

a is list(a) # False

from pickle import *
a == copy.deepcopy(a)
a is copy.deepcopy(a)

# 속도
import numpy as np
np.std(numpy_rands)

# 리스트
a = list()
a = []
a
a.append(1)
a.insert(3, 5)
a.insert(3, 4)
a.append('안녕')
a.append(True)

a[3]
a[1:3] # index 1부터 2까지
a[:3]
a[4:]
a[1:4]
a[1:4:2] # index 1부터 3까지 홀수번째만
a[9] # 존재하는 인덱스 조회 (IndexError)

# try-excep 예외처리
try:
    print(a[2])
except IndexError:
    print('존재하지 않는 인덱스')

# 요소 삭제
a
del a[1] # delete by index
a
a.remove(4)
a # delete by value
a.pop(3) # stack
a

# dictionary
a = dict()
a = {}
a = {'key1':'value1', 'key2':'value2'}
a
a['key3'] = 'value3'
a
a['key1']
a['key4'] # 존재하지 않는 key 조회: KeyError

# keyerror 예외처리
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

del a['key4'] # 존재하지 않는 key delete: KeyError

# 키 존재 유무 사전에 확인하는 방법
'key4' in a
if 'key4' in a:
    print('존재하는 키')
else:
    print('존재하지 않는 키')

# look up by for statement
for k,v in a.items():
    print(k,v)
a

del a['key1']
a

# Dictionary Module
# defaultdict
import collections
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
a
a['C'] += 1 # 존재하지 않는 키에 대해서도 디폴트 값 할당
a

# Counter object
a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
b # key: item, value: count
type(b)

# most common
b.most_common(2)

# OrderedDict object
# 입력 순서가 유지되는 자료형
a = collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})
print(a)

# data type declare
type([])
type(())
type({})
type({1})