import requests


def Log(stack, level, package, message):
    body = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }
    headers={"Authorization":
    "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiIyMjAzMDMxMDUwNTU5QHBhcnVsdW5pdmVyc2l0eS5hYy5pbiIsImV4cCI6MTc1MDY2NjUwOSwiaWF0IjoxNzUwNjY1NjA5LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiNjBmNzJiZWQtYTgxNy00MjliLTk0ZTEtMmE3OGQ2Nzc4YzY4IiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoicmF4aXRrdW1hciBsaWxhZGhhcmJoYWkgZ2FtZGhhIiwic3ViIjoiNjg3NWIwZmEtZGQ1YS00MmUxLThlNDMtZjJhOWIwMmZmYzkxIn0sImVtYWlsIjoiMjIwMzAzMTA1MDU1OUBwYXJ1bHVuaXZlcnNpdHkuYWMuaW4iLCJuYW1lIjoicmF4aXRrdW1hciBsaWxhZGhhcmJoYWkgZ2FtZGhhIiwicm9sbE5vIjoiMjIwMzAzMTA1MDU1OSIsImFjY2Vzc0NvZGUiOiJUUnpnV00iLCJjbGllbnRJRCI6IjY4NzViMGZhLWRkNWEtNDJlMS04ZTQzLWYyYTliMDJmZmM5MSIsImNsaWVudFNlY3JldCI6ImRRa1RUaHl1UFFkSEdnZ0QifQ.MG2tPV72xcaEFolNPj0b4XAsTmU2sYQpaea_aD_q7-4"
    }

    r = requests.post("http://20.244.56.144/evaluation-service/logs", json=body, headers=headers)
    if(r.status_code == 200):
        print(r.text)
    else:
        print(r.status_code,"\n", r.text)

Log("backend", "error", "handler", "checking middleware log")