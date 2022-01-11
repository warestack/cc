import requests
import json
import sys

data = requests.get(sys.argv[1]).json()
count = {'under':0,'over':0}
for k,v in data.items():
    print(k,v)
    if v>=50:
      count['over']+=1
    else:
      count['under']+=1
print(count)