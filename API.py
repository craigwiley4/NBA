'''import http.client

conn = http.client.HTTPSConnection("api-basketball.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "api-basketball.p.rapidapi.com",
    'x-rapidapi-key': "d72fc9bf51msh557bce8dfa4e4d3p15b58cjsn372562156e0f"
    }

conn.request("GET", "/teams?name=Washington%20Wizards", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
'''

import http.client

conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "d72fc9bf51msh557bce8dfa4e4d3p15b58cjsn372562156e0f",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }

conn.request("GET", "/games/gameId/500", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
