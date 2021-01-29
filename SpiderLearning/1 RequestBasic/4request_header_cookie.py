"""
@Time : 2021/1/29 9:54 
@Author : Steven Chen
@File : 4request_header_cookie.py 
@Software: PyCharm
"""
# 目标：
# 方法：
import requests
url = 'https://github.com/PandaCoding2020'
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53",
    "cookie": "_octo=GH1.1.358692347.1554840020; _ga=GA1.2.59697938.1554840020; _device_id=60d9769fd3fdc2235abf6fdd29b31a97; user_session=kKzwErWaCQYaFMH0lrjSTfLNpSoXLKhCB3NBaUPYl8FejzWl; __Host-user_session_same_site=kKzwErWaCQYaFMH0lrjSTfLNpSoXLKhCB3NBaUPYl8FejzWl; logged_in=yes; dotcom_user=PandaCoding2020; has_recent_activity=1; tz=Asia%2FShanghai; _gh_sess=rlQUfViTvHnD9iR5XhwxzbrymK7xwYYHJ1vdRGB9vAonJRFKZk2duKjpGhvr4UwZqwRpZeOiDTfwMdnsPAwn6hjm4GNYxY7xzJK05u1%2FdwqhIgZBmGNgG7s4gDvqwiEqSA%2BbA14DGgqRCCYHsFloCToW0e7wLzGrtCMBgMNv8tx67QbyP4BaMyBxgHc%2FO%2F2Z--HcrZEvIzY1UFGgaL--tFLMqsWygO75tY5xHBRqYw%3D%3D"
}

response = requests.get(url, headers = headers)

with open('github_without.html','wb') as f:
    f.write(response.content)