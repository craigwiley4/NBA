import http.client

conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "d72fc9bf51msh557bce8dfa4e4d3p15b58cjsn372562156e0f",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
    }

conn.request("GET", "/games/seasonYear/2020", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
