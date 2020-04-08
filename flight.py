"""
@author:Areej&ZRM
@file:app.py

"""

from amadeus import Client, ResponseError




def get_flight(start_place_code, end_place_code, start_data,traveller):
    client = Client(
        client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
        client_secret='IWBwclckwNgBKNWr'
    )
    # try:
    response = client.shopping.flight_offers_search.get(
        originLocationCode=start_place_code,
        destinationLocationCode=end_place_code,
        departureDate=start_data,
        adults=traveller)
    return response
    # except ResponseError as error:
    #     print(str(error))

