import json
import requests


payload={
    "name":"API",
    "job":"API Testing"
        }
resp =requests.post("https://reqres.in/api/users",data=payload)
print(resp)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()['job']=='API Testing'