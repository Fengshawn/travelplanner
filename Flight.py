from amadeus import Client, ResponseError
from locations import get_location


def get_flight(start_place_code, end_place_code, start_date,traveller):
    client = Client(
        client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
        client_secret='IWBwclckwNgBKNWr'
    )
    # try:
    flight_data_dict = {}
    response = client.shopping.flight_offers_search.get(
        originLocationCode=start_place_code,
        destinationLocationCode=end_place_code,
        departureDate=start_date,
        adults=traveller)

    flight_data_dict["price"] = f"{response.data[0]['price']['total']} {response.data[0]['price']['currency']}"
    flight_data_dict["departure_airport"] = response.data[0]['itineraries'][0]['segments'][0]['departure']['iataCode']
    flight_data_dict["arrival_airport"] = response.data[0]['itineraries'][0]['segments'][0]['arrival']['iataCode']
    date_time_dep = response.data[0]['itineraries'][0]['segments'][0]['departure']['at'].split('T')
    flight_data_dict["departure_dtime"] = f"Date: {date_time_dep[0]} Time: {date_time_dep[1]}"
    date_time_arr = response.data[0]['itineraries'][0]['segments'][0]['arrival']['at'].split('T')
    flight_data_dict["arrival_dtime"] = f"Date: {date_time_arr[0]} Time: {date_time_arr[1]}"
    flight_data_dict["aircraft_code"] = response.data[0]['itineraries'][0]['segments'][0]['aircraft']['code']
    flight_data_dict['duration'] = response.data[0]['itineraries'][0]['segments'][0]['duration'].replace("PT", "").replace("H", " Hours ").replace("M", " Minutes")
    return flight_data_dict
    # except ResponseError as error:
    #     print(str(error))


if __name__ == '__main__':

    resp = get_flight(str(get_location("Dubai")), str(get_location("London")), "2020-05-02", 2)
    print("Done")