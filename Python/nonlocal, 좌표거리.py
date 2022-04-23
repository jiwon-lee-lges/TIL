def solution(numbers, hand):
    answer = ''
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2], 
              4: [1, 0], 5: [1, 1], 6: [1, 2], 
              7: [2, 0], 8: [2, 1], 9: [2, 2], 
              '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    
    now_left = '*'
    now_right = '#'
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            now_left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            now_right = number
        else:
            x = keypad[number][0]
            xl = keypad[now_left][0]
            xr = keypad[now_right][0]
            
            y = keypad[number][1]
            yl = keypad[now_left][1]
            yr = keypad[now_right][1]

            if abs(x-xl) + abs(y-yl) > abs(x-xr) + abs(y-yr):
                answer += 'R'
                now_right = number
            elif abs(x-xl) + abs(y-yl) < abs(x-xr) + abs(y-yr):
                answer += 'L'
                now_left = number
            else:
                if hand == "left":
                    answer += 'L'
                    now_left = number
                else:
                    answer += 'R'
                    now_right = number
                    
            
    return answer
  
  ### 좌표간 거리 구할 때 sqrt((x1-x2)^2 + (y1-y2)^2) 대신에 abs(x1-x2) + abs(y1-y2)로 해야 통과됨
