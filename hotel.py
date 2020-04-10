"""
@author:Areej
@file:hotel.py

"""
from Models import hotel
from amadeus import Client
from opencage.geocoder import OpenCageGeocode



def get_hotel(place):
    """

    :param place_code: suggests the best hotel deal based on the city selected
    :return:
    """
    client = Client(
        client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
        client_secret='IWBwclckwNgBKNWr'
    )

    key = "25cff282b29f43b9ac3aad454f1945a6"
    geocoder = OpenCageGeocode(key)  # Gecoding Service to get coordinates of city
    result = geocoder.geocode(place, no_annotations='1')  # Geo-coding Service API key
    longitude = result[0]['geometry']['lng']  # Parsing Latitude
    latitude = result[0]['geometry']['lat']  # Parsing Longitude
    response = client.shopping.hotel_offers.get(latitude=latitude, longitude=longitude)
    hotel_dict = {}
    try:
        selected_hotel = response.data[0]
        #print(response.data)
    except IndexError:
        return {'name': 'N/A', 'address': 'N/A', 'rate': 'N/A'}
    hotel_dict['name'] = selected_hotel['hotel']['name']
    hotel_dict['address'] = selected_hotel['hotel']['address']['lines'][0]
    hotel_dict['rate'] = f"{selected_hotel['offers'][0]['price']['total']} {selected_hotel['offers'][0]['price']['currency']}"
    hotel_dict['contact'] = selected_hotel['hotel']['contact']['phone']

    #class for deal later logic business
    hotel_temp=hotel(selected_hotel['hotel']['name'],f"{selected_hotel['offers'][0]['price']['total']} {selected_hotel['offers'][0]['price']['currency']}",
                     selected_hotel['hotel']['address']['lines'][0],selected_hotel['hotel']['contact']['phone'])

    return hotel_dict


if __name__ == '__main__':
    resp = get_hotel('London')
    #print(resp)
    print("Done!")