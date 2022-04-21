# 힙(Heap)


```python
# 이진 힙 구현
class BinaryHeap(object): # 인덱스 0 비워둠
    def __init__(self):
        self.items = [None]
        
    def __len__(self): # 마지막 요소의 인덱스 가져오기 위함
        return len(self.items) - 1
```


```python
# 삽입 -> heapq.heappush()
def _percolate_up(self):
    i = len(self) # index
    parent = i // 2 # 레벨 별 인덱스가 2배가 되므로
    while parent > 0:
        if self.items[i] < self.items[parent]:
            self.items[parent], self.items[i] = self.items[i], self.items[parent]
        
        i = parent
        parent = i // 2 # 위의 단계 반복
```


```python
def insert(self, k):
    self.items.append(k) # 배열의 맨 마지막에 할당
    self._percolate_up() # 부모노드와 자리 바꾸기
```


```python
# 추출
# 수도코드 (최대 힙)
Max-Heapify(A, i):
    left <- 2 * i
    right <- 2 * i + 1
    largest <- i
    
    if left <= heap_length[A] and A[left] > A[largest] then:
        largest <- left
    
    if right <= heap_length[A] and A[right] > A[largest] then:
        largest <- right
    
    if largest != i then:
        swap A[i] and A[largest]
        Max-Heapify(A, largest)
```


```python
# 이진 힙의 인덱스 위치 계산 수도코드
# 1번 인덱스부터 사용하는 이유
Parent(i)
    return cell((i - 1) / 2)

Left(i)
    return 2 * i

Right(i)
    return 2 * i + 1
```


```python
# 최소 힙 알고리즘 구현
def _percolate_down(self, idx):
    left = idx * 2
    right = idx * 2 + 1
    smallest = idx
    
    if left <= len(self) and self.items[left] < self.items[smallest]:
        smallest = left
    
    if right <= len(self) and self.items[right] < self.items[smallest]:
        smallest = right
        
    if smallest != idx:
        self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx] # swap
        self._percolate_down(smallest)
```


```python
# 추출 -> heapq.heappop()
def extract(self):
    extracted = self.items[1] # 루트 값 추출
    self.items[1] = self.items[len(self)]
    self.items.pop()
    self._percolate_down(1)
    return extracted
```


```python
# 전체 코드
class BinaryHeap(object):
    def __init__(self):
        self.items = [None] # 인덱스 0 삭제
    
    def __len__(self):
        return len(self.items) - 1 # 마지막 요소의 인덱스 가져오기
    
    # 삽입시 실행, 반복 구조 구현
    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent] # swap
            i = parent
            parent = i // 2
            
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()
        
    #추출시 실행, 재귀 구조 구현
    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx
        
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        
        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx] # swap
            self._percolate_down(smallest)
    
    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted
```


```python

```
