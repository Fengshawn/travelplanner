import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

querystring = {"query":"London","inboundpartialdate":"2019-12-01","outboundpartialdate":"2020-03-03"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "46b751a557msh32739197dd6a45bp150eaejsne5e6f4e93680"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)