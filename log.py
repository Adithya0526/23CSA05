import requests
log_url = r"http://4.224.186.213/evaluation-service/logs"
headers={
    "Content-Type":"application/json",
    "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJzYWRpdGh5YS5zMjU2QGdtYWlsLmNvbSIsImV4cCI6MTc4Mjc5OTczOSwiaWF0IjoxNzgyNzk4ODM5LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiNzA1MDkwYmItNmU4MS00OTY0LTljNTItZmIyNDA0ZjcwODA2IiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoiYWRpdGh5YSBzIiwic3ViIjoiNjJhMDhlODctNjFmMi00YTY4LTlhODQtMWU5NDJjNmU3MDJkIn0sImVtYWlsIjoic2FkaXRoeWEuczI1NkBnbWFpbC5jb20iLCJuYW1lIjoiYWRpdGh5YSBzIiwicm9sbE5vIjoiMjNjc2EwNSIsImFjY2Vzc0NvZGUiOiJXak55Q1QiLCJjbGllbnRJRCI6IjYyYTA4ZTg3LTYxZjItNGE2OC05YTg0LTFlOTQyYzZlNzAyZCIsImNsaWVudFNlY3JldCI6IlNBYmJjQm51WHRuZVFHcUgifQ.0gAjS84wdFG__lr4Mx3R1w6-LlzYRXM-6gS8lLl4JYo"
}
def Log(stack,level,package,message):
    logs={
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }
    try :
        response=requests.post(log_url,json=logs,headers=headers)
        print(response.status_code)
        print(response.json())
    except Exception as e:
        print("Error while sending logs:",e)