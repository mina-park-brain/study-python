''' Postman > Basic Auth
	(÷�ε� �̹��� ���� ���� : 00_Postman_BasicAuth.JPG)
'''
import requests

s = requests.Session()
s.auth = ('postman', 'password')

r = s.get("https://echo.getpostman.com/basic-auth")
print(r.text)

