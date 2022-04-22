# 주석과 적절한 변수명 설정의 필요성
def numMatchingSubseq(self, S: str, words: List[str]) -> int:
    a = 0

    for b in words:
        c = 0
        for i in range(len(b)):
            d = S[c:].find(b[i])
            if d < 0:
                a -= 1
                break
            else:
                c += d + 1
        a += 1

    return a

# 더 나은 코드
def numMatchSubseq(self, S: str, words: List[str]) -> int:
    matched_count = 0

    for word in words:
        pos = 0
        for i in range(len(word)):
            # Find matching position for each character
            found_pos = S[pos:].find(word[i])
            if found_pos < 0:
                matched_count -= 1
                break
            else: # If found, take step position forward.
                pos += found_pos + 1
        matched_count += 1 

    return matched_count

# list comprehension
# 가독성이 저해되는 경우
strls = [
    strl[i:i + 2].lower() for i in range(len(strl) - 1)
    if re.findall('[a-z]{2}', strl[i:i + 2].lower())
]

# 가독성을 향상시키려면
# list comprehension은 표현식이 2개를 넘지 않도록
strls = []
for i in range(len(strl) - 1):
    # 연속해서 나오는 문자 추출
    if re.findall('[a-z]{2}', strl[i:i + 2].lower()):
        strls.append(strl[i:i + 2].lower())


# 표현식을 여러 줄에 걸쳐 표현하는 경우
return [(x, y, z)
        for x in range(5)
        for y in range(5)
        if x != y
        for z in range(5)
        if y != z
        ]

# google python style guide
# 1 가변객체 사용을 지양하자
def foo(a, b = []):
    ...
def foo(a, b: Mapping = {}):
    ...

# 2 불변객체를 사용하자
def foo(a, b=None):
    if b is None:
        b = []

def foo(a, b: Optional[Sequence] = None):
    if b is None:
        b = []

# 3 True/False는 암시적 방법을 사용하자
if not users:
    print('no users')

# 명시적으로 값을 비교하자
if foo == 0:
    self.handle_zero()

if i % 10 == 0:
    self.handle_multiple_of_ten()

# 3-1 잘못된 사용법
if len(users) == 0:
    print('no users')

if foo is not None and not foo:
    self.handle_zero()

if not i % 10:
    self.handle_multiple_of_ten()

# Zen of Python
import this

python -m pip install this
