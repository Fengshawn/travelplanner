"""
@author:ZRM
@file:get_place_of_interest.py
@time:2020/03/27
"""

from amadeus import Client, ResponseError

amadeus = Client(client_id="YhUHykQeccgseWSSARlxtfIAzhdGgTM2", client_secret="IWBwclckwNgBKNWr")
try:
    response = amadeus.reference_data.locations.points_of_interest.get(latitude=51.510351, longitude=-0.1316944)
    print(response.data)

except ResponseError as error:
    print(error)
