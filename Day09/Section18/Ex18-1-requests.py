'''
모듈 설치
pip install requests
'''

import requests

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code': 161067}
response = requests.get(url, params=param)
print(response.text)
