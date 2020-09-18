import requests

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
get_url = requests.get(url)

with open('logs.txt' , 'wb') as m:
  m.write(get_url.content)

total_lines = 0
yr_1995 = 0
yr_1994 = 0

m = open('logs.txt', "r")

lines = m.readlines()

for line in lines:
  total_lines = total_lines + 1
  if line.find("1995") != -1:
    yr_1995 = yr_1995 + 1
  if line.find("1994") != -1:
    yr_1994 = yr_1994 + 1

m.close()

print("Total lines in file: ", total_lines)
print("Requests made in the last year of 1995: ", yr_1995)
print("I got curious about 1994: ", yr_1994)
print("True total requests made: ", yr_1994 + yr_1995)
print("Total possible broken reuqests: ", total_lines - (yr_1994 + yr_1995))
