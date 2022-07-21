import requests


BASE = 'http://127.0.0.1:5000/'

data =  [{"likes": 10,  "name": 'melissa', "views": 1000000}, 
         {"likes": 3,  "name": 'how to make a REST api', "views": 508},
         {"likes": 100, "name": 'oliver catches fish on cat tv', "views": 7000000}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()  
response = requests.delete(BASE + "video/0")
print(response)


input()
response = requests.get(BASE + 'video/2')
print(response.json())



