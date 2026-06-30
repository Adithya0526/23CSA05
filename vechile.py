import log
from flask import jsonify
import requests
token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJzYWRpdGh5YS5zMjU2QGdtYWlsLmNvbSIsImV4cCI6MTc4MjgwMzk4OSwiaWF0IjoxNzgyODAzMDg5LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiMzBkYzg3OTktZDYwYy00ZWI3LTkzODUtYzQ2N2QyZjFjMWJiIiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoiYWRpdGh5YSBzIiwic3ViIjoiNjJhMDhlODctNjFmMi00YTY4LTlhODQtMWU5NDJjNmU3MDJkIn0sImVtYWlsIjoic2FkaXRoeWEuczI1NkBnbWFpbC5jb20iLCJuYW1lIjoiYWRpdGh5YSBzIiwicm9sbE5vIjoiMjNjc2EwNSIsImFjY2Vzc0NvZGUiOiJXak55Q1QiLCJjbGllbnRJRCI6IjYyYTA4ZTg3LTYxZjItNGE2OC05YTg0LTFlOTQyYzZlNzAyZCIsImNsaWVudFNlY3JldCI6IlNBYmJjQm51WHRuZVFHcUgifQ.xfa2hyoPCfTvz7YG8gARg8ogOaiacl5p9GxWmqFJCtQ"
headers={
    "Content-Type":"application/json",
    "Authorization":"Bearer " + token
}
depotURL = r"http://4.224.186.213/evaluation-service/depots"
vechileURL = r"http://4.224.186.213/evaluation-service/vehicles"
depots=requests.get(depotURL,headers=headers).json()
log.Log("backend","info","handler","Depots fetched successfully")
vehicles=requests.get(vechileURL,headers=headers).json()
log.Log("backend","info","handler","Vehicles fetched successfully")
