import requests

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
get_url = requests.get(url)

with open('logs.txt' , 'wb') as m:
  m.write(get_url.content)

tr = 0
yr = 0
extra = 0

m = open('logs.txt', "r")

lines = m.readlines()

for line in lines:
  tr = tr + 1
  if line.find("1995") != -1:
    yr = yr + 1
  if line.find("1994") != -1:
    extra = extra + 1   

m.close()

print(tr)
print(yr)
print("I got curious about 1994: ", extra)
print("Calculation check: ", yr + extra)
