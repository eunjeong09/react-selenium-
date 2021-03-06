from selenium import webdriver
import time
# 크롬 드라이버가 설치된 경로
driver = webdriver.Chrome('/Users/go-eunjeong/Desktop/chromedriver')
driver.implicitly_wait(2)
# 접속할 주소 입력
driver.get('http://172.20.10.4:3000')


# 나에게 카카오톡 메시지를 보내는 함수
def sendMessage():
    import requests
    import json

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # 사용자 토큰
    # headers = {"Authorization": "Bearer !!!발급받은 토큰 넣기!!! "}


    data = {
        "template_object" : json.dumps({ "object_type" : "text",
                                         "text" : "경고! 카운터가 음수입니다.",
                                         "link" : {
                                                     "web_url" : "https://developers.kakao.com"
                                                  }
        })
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    if response.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))


# 현재 카운터를 체크하는 함수
def checkCounter():
    counter = driver.find_element_by_id('counter').text
    print(counter)
    if(int(counter) < 0):
        sendMessage()

# 버튼 누르는 부분
for i in range(3):
    time.sleep(1)
    driver.find_element_by_id('plus').click()
    checkCounter()
for j in range(4):
    time.sleep(1)
    driver.find_element_by_id('minus').click()
    checkCounter()

# 크롬 드라이버 닫기
driver.close()




