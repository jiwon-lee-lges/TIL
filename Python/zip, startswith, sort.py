def solution(phone_book):
    ## phone_book.sort()는 원래 리스트도 반영
    ## sorted(phone_book)은 정렬된 리스트 반환/원래 리스트에는 반영하지 않음
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    
    return True

### 문자열은 정렬하면 자릿수와 관계없이 첫 자리부터 차례대로 값을 비교함
### zip 함수는 두 리스트를 압축하는 기능
### startswith 함수는 T/F를 반환함
