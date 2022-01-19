import json
import random
dict1 = {'server'+str(k): random.randint(1,100) for (k, v) in enumerate(range(10))}
data = json.dumps(dict1)
print(data)

with open('/var/www/html/data.json', 'w') as outfile:
   json.dump(dict1, outfile)

print("Done!")
