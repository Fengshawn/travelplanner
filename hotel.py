"""
@author:Areej
@file:hotel.py

"""
from Models import hotel
from amadeus import Client
from opencage.geocoder import OpenCageGeocode


def get_hotel(place, days):
    """

    :param place_code: suggests the best hotel deal based on the city selected
    :return:
    """
    client = Client(
        client_id='HmVt5vGJBXOCBhwJ3oHOMzDJQYuLCIpj',
        client_secret='cRxFUJZYWEAQtobG'
    )
    key = "25cff282b29f43b9ac3aad454f1945a6"
    geocoder = OpenCageGeocode(key)  # Gecoding Service to get coordinates of city
    result = geocoder.geocode(place, no_annotations='1')  # Geo-coding Service API key
    # here we get only london (there will be many london in the world)
    longitude = result[0]['geometry']['lng']  # Parsing Latitude
    latitude = result[0]['geometry']['lat']   # Parsing Longitude
    response = client.shopping.hotel_offers.get(latitude=latitude, longitude=longitude, currency='GBP')
    print(response.data)
    # get all hotel number in london
    hotel_number = len(response.data)
    # use a list to store hotel information
    all_hotel = []
    hotel_contact = "NULL"
    hotel_address = "NULL"
    hotel_name = "NULL"
    hotel_rating = "4"
    hotel_price = 95
    hotel_latitude = 0
    hotel_longitude = 0
    hotel_unit = 'GBP'
    # only choose top 3
    if (hotel_number <= 3):
        for temp_hotel in response.data:
            if 'name' in temp_hotel['hotel'].keys():
                hotel_name = temp_hotel['hotel']['name']
            if 'rating' in temp_hotel['hotel'].keys():
                hotel_rating = temp_hotel['hotel']['rating']
            if 'address' in temp_hotel['hotel'].keys() and 'lines' in temp_hotel['hotel']['address'].keys():
                hotel_address = temp_hotel['hotel']['address']['lines'][0]
            if 'hotel' in temp_hotel['hotel']['contact'].keys() and 'phone' in temp_hotel['hotel']['contact'].keys():
                hotel_contact = temp_hotel['hotel']['contact']['hotel']
            if 'latitude' in temp_hotel['hotel'].keys():
                hotel_latitude = temp_hotel['hotel']['latitude']
            if 'longitude' in temp_hotel['hotel'].keys():
                hotel_longitude = temp_hotel['hotel']['longitude']
            if 'price' in temp_hotel['offers'][0].keys() and 'total' in temp_hotel['offers'][0]['price'].keys():
                hotel_price = temp_hotel['offers'][0]['price']['total']
            if 'price' in temp_hotel['offers'][0].keys() and 'currency' in temp_hotel['offers'][0]['price'].keys():
                hotel_unit = temp_hotel['offers'][0]['price']['currency']
            hotel_prase = hotel(name=hotel_name, unit=hotel_unit, rate=hotel_rating, price=hotel_price,
                                latitude=hotel_latitude, longitude=hotel_longitude, communication=hotel_contact,
                                days=days,
                                position=hotel_address)
            all_hotel.append(hotel_prase)

    else:
        for temp_hotel in response.data[0:3]:

            if 'name' in temp_hotel['hotel'].keys():
                hotel_name = temp_hotel['hotel']['name']
            if 'rating' in temp_hotel['hotel'].keys():
                hotel_rating = temp_hotel['hotel']['rating']
            if 'address' in temp_hotel['hotel'].keys() and 'lines' in temp_hotel['hotel']['address'].keys():
                hotel_address = temp_hotel['hotel']['address']['lines'][0]
            if 'contact' in temp_hotel['hotel'].keys() and 'phone' in temp_hotel['hotel']['contact'].keys():
                hotel_contact = temp_hotel['hotel']['contact']['phone']
            if 'latitude' in temp_hotel['hotel'].keys():
                hotel_latitude = temp_hotel['hotel']['latitude']
            if 'longitude' in temp_hotel['hotel'].keys():
                hotel_longitude = temp_hotel['hotel']['longitude']
            if 'price' in temp_hotel['offers'][0].keys() and 'total' in temp_hotel['offers'][0]['price'].keys():
                hotel_price = temp_hotel['offers'][0]['price']['total']
            if 'price' in temp_hotel['offers'][0].keys() and 'currency' in temp_hotel['offers'][0]['price'].keys():
                hotel_unit = temp_hotel['offers'][0]['price']['currency']
            hotel_prase = hotel(name=hotel_name, unit=hotel_unit, rate=hotel_rating, price=hotel_price,
                                latitude=hotel_latitude, longitude=hotel_longitude, communication=hotel_contact,
                                days=days,
                                position=hotel_address)
            all_hotel.append(hotel_prase)
    return all_hotel[0]


if __name__ == '__main__':
    pass
    resp = get_hotel('London')
    print(resp.latitude)
    print(resp.longitude)
    print("Done!")
