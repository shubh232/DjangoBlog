import requests
import bs4
response = requests.session()

url = "http://14.139.233.57/mmmut/StudentLogin.aspx"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTTARGET\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTARGUMENT\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__VIEWSTATE\"\r\n\r\n/wEPDwULLTE0OTQ2MTUzMzZkZAc4SbtTSHLUbg0ViOvVOr4HkFr1w6l+FiUUfNXadonr\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTVALIDATION\"\r\n\r\n/wEdAAbO3LImvAZ6n/EuT78+opQuY3plgk0YBAefRz3MyBlTcHY2+Mc6SrnAqio3oCKbxYainihG6d/Xh3PZm3b5AoMQRFGbj2vrNrQTo53xeYkuF9lIETJhURQdME90gSeMN4R7Xe2ZfLJNil7n6yzSP73lQGo4ohzA1gzSJQHXagjQcA==\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"txtUserName\"\r\n\r\nshubh232@gmail.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"txtPassword\"\r\n\r\nsftr96rs\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"btnLogin\"\r\n\r\nSubmit\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "cb28a4c7-8e41-0728-8a93-f881f47a7146"
}

c = response.request("POST", url, data=payload, headers=headers)
print(response.cookies.keys())
b = bs4.BeautifulSoup(c.text,'html.parser')
a = b.select('a[href*="grdattendance"]')
print(a)