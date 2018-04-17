import requests

headers = {}

headers['Authorization'] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTIzOTk1NzM5LCJqdGkiOiJiM2FmNTBlN2UwZjc0NGJlYjhjNDRmMGRmMTdkMjEzMyIsInVzZXJfaWQiOjF9.mxRPDLhPXCBCoyiYIjxVIq_yqB73dgEy95elHxZ5_9s"

r = requests.get('http://127.0.0.1:8000/paradigms/', headers=headers)

print(r.text)