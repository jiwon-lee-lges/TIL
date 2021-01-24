#!/usr/bin/env python
# coding: utf-8

# 
# # [고급프로그래밍 학기말 과제 - 2017280063 경제학부 이지원]
# 
# ## 프로그램 설계 보고서
# 
# > 프로그램 구현을 위해 tkinter 모듈과 random 모듈을 사용합니다.

# In[116]:


from tkinter import *
import random, string


# ## 1. tkinter 모듈을 활용한 컨테이너 생성
# 
# > 먼저, 프로그램을 담아줄 컨테이너 틀을 잡습니다. tkinter 모듈 내 grid 메소드를 통해 각 기능의 위치를 잡아줍니다. 또한, 버튼 클래스를 사용하여 당첨번호를 출력하도록 하였고, 추후 함수를 정의해 할당해 줍니다. 
# 
# ###     ** 추가한 옵션 **
# 
# > 기존 로또 프로그램과 달리, 사용자가 원하는 숫자를 반드시 포함하도록 설계했습니다. 이는 추후 lotto() 함수에서 입력값으로 활용합니다.

# In[114]:


window = Tk()
window.title('Lotto')
window.geometry('300x200')

label = Label(window, text = '로또 게임')
Label(window, text = '포함하고 싶은 넘버').grid(column = 0, row = 0)
Label(window, text = ' ').grid(column = 1, row = 1)

res_label = Label(window, text ='')
res_label.grid(column = 1, row = 4)


num1 = Entry(window, width = 10)
num1.grid(column = 1, row = 0)

btn = Button(window, text = '행운의 당첨번호는?', bg = 'green', command = lotto)
btn.grid(column = 1, row = 3)

window.mainloop()


# ## 2. random 모듈을 활용한 로또 번호 생성기 구현
# 
# > 다음으로, random 모듈을 활용하여 버튼에 할당될 로또 번호 생성기를 구현합니다. 로또 번호는 1~46까지의 숫자들 중 random 하게 발생시키는데, 비복원 임의 추출 방식을 따르고, 난수 seed는 시스템의 현재시간을 참조하도록 합니다. (random.seed(a = None)) 
# 
# > 또한, 사용자가 선택한 숫자를 제외해야 하므로, 1~46까지 원소를 담은 리스트에서 사용자가 선택한 수를 제외한 뒤, 전체 6개 자리 숫자 중 5개의 수만 추출합니다.
# 
# > 마지막으로 추출한 수를 sort() 함수를 사용하여 정렬해 위의 res_label 라벨의 text 자리에 할당합니다.

# In[ ]:


def lotto(): 

    cont = True
    while cont:
        num = num1.get()
        
        if (num.isdigit() == True):
            
            lst = list(range(1, 47))
            lst.remove(int(num))
            
            random.seed(a = None)
            lotto = random.sample(lst, 5)
            lotto.append(int(num))
            lotto.sort()

            res_lotto = lotto
            res_label.configure(text = res_lotto)
            cont = False
        else:
            break


# ## 3. 조건 확인
# 
# > 위의 난수 생성 매커니즘이 주어진 조건 (각 숫자의 비율이 5% 이상 차이나지 않도록) 을 만족하는지 확인합니다. 이를 위해 동일한 시드로 로또 번호를 생성하여 하나의 리스트 (res)에 담아줍니다.
# 
# > 이때, 비율을 확인할 표본은 600개 (6개씩 100번)로 설정했습니다.

# In[117]:


cont = True
while cont:
    
    lst = list(range(1, 47))
        
    lotto = []
    for i in range(100):
        
        random.seed(a = None)
        lotto.insert(1, random.sample(lst, 6))
        cont = False


# In[118]:


res = []
for i in range(len(lotto)):
    for j in range(6):
        res.append(lotto[i][j])


# In[119]:


print(res, end ='')


# ## 3-1) numpy 모듈을 활용해 각 숫자의 출현 빈도 구하기
# 
# > python의 numpy 모듈을 np로 불러와 unique 메소드를 사용합니다. 그 결과, 1부터 46까지의 숫자가 counts만큼 추출되었음을 확인할 수 있습니다. 

# In[120]:


import numpy as np
unique, counts = np.unique(res, return_counts = True)


# In[121]:


unique


# In[79]:


counts


# ## 3-2) 각 숫자의 출현 비율 구해 조건을 만족하는지 확인하기
# 
# > 위의 결과를 바탕으로 각 숫자의 출현 빈도가 전체 원소 수 (600개)에 대해 얼마만큼의 비중을 갖고 있는지 확인해봅니다. 
# 
# > 총 46개의 숫자의 출현 비율이 5%가 넘어가지 않도록 하는 조건을 만족하였음을 확인할 수 있습니다. 

# In[122]:


res1 = []
for i in range(len(counts)):
    res1.append(counts[i] / sum(counts))


# In[123]:


print(res1, end ='')


# In[ ]:




