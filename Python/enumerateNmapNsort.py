def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
  
  ### enumerate 함수로 인덱스와 값을 매칭시켜줌 -> 인덱스가 리스트 내 해당 값 이상의 값을 갖는 개수임
  ### 인덱스, 값 중 작은 값들을 answer의 후보군으로 뽑은 후 문제의 지시에 따라 max로 최대 값을 최종 answer로 정함
