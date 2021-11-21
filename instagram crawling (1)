import requests
import datetime

header = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'ig_did=D0394F58-9F97-40FB-AF0F-3378E9882036; ig_nrcb=1; mid=YZqDbQALAAHTzF_eggxJxG7n7jFp; csrftoken=MpYKvMzfh1XSUxzBcwSkkgCNyOv53goz; ds_user_id=5766088200; sessionid=5766088200%3AS3WK28umSry7Rn%3A17; shbid="17933\0545766088200\0541669052164:01f75239ec0cab316a29e5eb534425953a097ff9d825359d6a0cf46a11ea451b210d483b"; shbts="1637516164\0545766088200\0541669052164:01f7183671e05716817348244a52bd84ba72d3e0d903ae08a1fc97ca6219dab63413ef40"; rur="EAG\0545766088200\0541669052175:01f7a8ddfa03bcbabdb773a7f49266084737ba0d6c60153167a4a3f057d030a422ee45ff"',
    'referer': 'https://www.instagram.com/explore/tags/%EB%8C%95%EB%8C%95%EC%9D%B4/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
    'x-asbd-id': '198387',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR28x2npEWUBb-Njoq3jak-Cgwpel9MzRyaY8Nse7I7lBVNJ',
    'x-requested-with': 'XMLHttpRequest'
}

# URL = 'https://www.instagram.com/explore/tags/%EB%8C%95%EB%8C%95%EC%9D%B4/?__a=1'
# res = requests.get(URL, headers=header)
# res = res.json()

# print(res)

# print(res.keys())
# print(res['data'].keys())

### top은 인기게시물, recent는 최근 게시물 들어 있음
### recent에는 최근 게시물부터 시간 순 정렬되어 있음
# print(res['data']['media_count']) # 14472203
# print(res['data']['profile_pic_url'])
# print(res['data']['recent'])

### recent의 key로는 next_page, next_max_id가 있음
### next_page = 1이면 다음 페이지가 있다는 의미, next_max_id는 다음 페이지를 열기 위한 id
### sections는 게시물 데이터가 들어있는 변수
# print(res['data']['recent'].keys()) # dict_keys(['sections', 'more_available', 'next_max_id', 'next_page', 'next_media_ids'])
# print(res['data']['recent']['next_page']) # 1
# print(res['data']['recent']['next_max_id']) # QVFDRnNFWldKSEJ1RS1wcmtPYjl6Qlk5T1lhOVRHblRIdkVhWERMYldDQWxKRG8zQThuajZ3ZU51a0NNWjBhYk16dmNYaGk0N3BiOUZ3MWJCMkN2RjJaRw==
# print(res['data']['recent']['next_media_ids']) # []

dataList = []
URL = 'https://www.instagram.com/explore/tags/댕댕이/?__a=1'
while(True):
    res = requests.get(URL, headers =header)
    res = res.json()
    if 'next_page' not in res['data']['recent'].keys() or int(res['data']['recent']['next_page']) == 0:
        break
    max_id = res['data']['recent']['next_max_id']

    for n in res['data']['recent']['sections']:
        for m in ((n['layout_content']['medias'])):
            m = m['media']
            data = {}
            data['keyword'] = '댕댕이'
            data['pagePk'] = m['code']
            data['URL'] = 'https://www.instagram.com/p/'+ data['pagePk']+"/"

            try:
                data['DatePublished'] = datetime.fromtimestamp(m['caption']['created_at'])
            except:
                continue
                data['Content'] = delrn(m['caption']['text'])

            try:
                data['reply'] = (m['comment_count'])
                data['replyList'] = (m['comments'])
            except:
                data['reply'] = 0
                data['replyList'] = []

            data['like'] = (m['like_count'])
            data['pk'] = str(m['pk'])
            data['user_full_name'] = (m['user']['full_name'])
            data['user_pk'] = str(m['user']['pk'])
            data['user_name'] = (m['user']['username'])
            data['user_profile'] = (m['user']['profile_pic_url'])

            dataList.append(data)

    URL = 'https://www.instagram.com/explore/tags/'+'댕댕이'+'/?__a=1&max_id='+max_id

print(dataList)
