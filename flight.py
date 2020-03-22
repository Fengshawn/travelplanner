from amadeus import Client, ResponseError

amadeus = Client(
    client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
    client_secret='IWBwclckwNgBKNWr'
)

def get_flight(start_place_code,end_place_code,start_data,traveller):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=start_place_code,
            destinationLocationCode=end_place_code,
            departureDate=start_data,
            adults=traveller)
        return response
    except ResponseError as error:
        print(error)

