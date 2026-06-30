from flask import jsonify
import requests
url=r"http://4.224.186.213/evaluation-service/auth"
data={
    "email":"sadithya.s256@gmail.com",
    "name":"Adithya S",
    "rollNo":"23CSA05",
    "accessCode":"WjNyCT",
    "clientID":"62a08e87-61f2-4a68-9a84-1e942c6e702d",
    "clientSecret":"SAbbcBnuXtneQGqH"
}
response=requests.post(url,json=data)
print(response.status_code)
print(response.json())

