from flask import jsonify
import requests
url=r"http://4.224.186.213/evaluation-service/register"
data={
    "email":"sadithya.s256@gmail.com",
    "name":"Adithya S",
    "mobileNo":"6383973794",
    "githubUsername":"Adithya0526",
    "rollNo":"23CSA05",
    "accessCode":"WjNyCT"
}
response=requests.post(url,json=data)
print(response.status_code)
print(response.json())

