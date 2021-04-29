import json
import requests


mydata =open("data.json","r").read()
resp =requests.post("https://reqres.in/api/users",data=json.loads(mydata))
print(resp)
print(resp.json())
assert resp.json()['job']=='Python Dev'