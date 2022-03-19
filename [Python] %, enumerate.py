def solution(answers) :
    tom = [1, 2, 3, 4, 5]
    suzy = [2, 1, 2, 3, 2, 4, 2, 5]
    rio = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for idx, answer in enumerate(answers):
        if answer == tom[idx%len(tom)]:
            score[0] += 1
        if answer == suzy[idx%len(suzy)]:
            score[1] += 1
        if answer == rio[idx%len(rio)]:
            score[2] += 1
    
    a = []
    for idx, s in enumerate(score):
        if s == max(score):
            a.append(idx+1)
    
    return sorted(a)

### 최고점을 받은 사람을 배열에 담아야 하므로, max(score)과 점수가 같은지를 체크해야 함
### enumerate 사용법 익히기
### % 연산자로 반복되는 구간에서 필요한 위치를 얻을 수 있음
