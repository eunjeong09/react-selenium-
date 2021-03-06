# 토큰 받는 부분
import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '!!!restAPI!!!'
redirect_uri = 'https://example.com/oauth'
authorize_code = '!!!인증 코드 입력!!!'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
with open(r"C:\Users\user\Desktop\PythonWorkspace\kakao_test\kakao_code.json","w") as fp:
    json.dump(tokens, fp)

#2.
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)