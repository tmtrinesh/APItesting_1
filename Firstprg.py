import requests

resp=requests.get("https://reqres.in/api/users?page=2")
code=resp.status_code
assert code==200,"Code doesn't match"
print(resp.text)
print(resp.content)
print(resp.json())
print(type(resp.headers))
print(resp.cookies)
print(resp.encoding)
print(resp.url)
json_response = resp.json()
print(json_response['total'])
assert json_response['total']==12
print(json_response['total_pages'])
assert json_response['total_pages']==2,"total pages count is not matching"
print(json_response["data"][0]["email"])#endswith("gmail.com"),"email format is not matching"
#assert (json_response["data"][0]["email"]).endswith("gmail.com"),"email format is not matching"