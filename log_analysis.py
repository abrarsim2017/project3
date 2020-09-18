import requests

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
get_url = requests.get(url, allow_redirects = True)

open('logs.txt' , 'wb').write(get_url.content)

lines = 0
requests = 0
