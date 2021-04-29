import json
import requests


payload={
    "name":"morpheus",
    "job":"Automation"
        }
resp =requests.post("https://reqres.in/api/users",data=payload)
print(resp)
print(resp.json())
assert resp.json()['job']=='Automation'