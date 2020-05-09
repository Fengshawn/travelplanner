from Models import hotel
from amadeus import Client
from opencage.geocoder import OpenCageGeocode


def hotel_postcode(args):
    pass


def get_hotel(place):
    client = Client(
        client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
        client_secret='IWBwclckwNgBKNWr'
    )

    key = "25cff282b29f43b9ac3aad454f1945a6"
    geocoder = OpenCageGeocode(key)  # Gecoding Service to get coordinates of city
    result = geocoder.geocode(place, no_annotations='1')  # Geo-coding Service API key
    # here we get only london (there will be many london in the world)
    response = client.shopping.hotel_offers.get(get_hotel(place))
    print(response.data)
    # get all hotel number in london
    hotel_number = len(response.data)
    # use a list to store hotel information
    all_hotel = []
    hotel_contact = "21432321"
    hotel_address = "A"
    hotel_postcode = "S2 4QF"
    hotel_name = "a"
    hotel_rating = "7"
    hotel_price = 150
    hotel_unit = 'GBP'
    # only choose top 3
    if (hotel_number <= 3):
        for temp_hotel in response.data:
            if ('name' in temp_hotel['hotel']):
                hotel_name = temp_hotel['hotel']['name']
            if ('rating' in temp_hotel['hotel']):
                hotel_rating = temp_hotel['hotel']['rating']
            if ('address' in temp_hotel['hotel'] and 'lines' in temp_hotel['hotel']['address']):
                hotel_address = temp_hotel['hotel']['address']['lines'][0]
            if ('contact' in temp_hotel['hotel'] and 'phone' in temp_hotel['hotel']['contact']):
                hotel_contact = temp_hotel['hotel']['contact']['hotel']
            if ('price' in temp_hotel['offers'][0] and 'total' in temp_hotel['offers'][0]['price']):
                hotel_price = temp_hotel['offers'][0]['price']['total']
            if ('postcode' in temp_hotel['hotel']):
                hotel_postcode = temp_hotel['hotel']['postcode']

            hotel_prase = hotel(name=hotel_name, unit=hotel_unit, rate=hotel_rating, price=hotel_price,
                                 communication=hotel_contact, postcode= hotel_postcode, position=hotel_address)
            all_hotel.append(hotel_prase)



    else:
        for temp_hotel in response.data[0:3]:
            if ('name' in temp_hotel['hotel']):
                hotel_name = temp_hotel['hotel']['name']
            if ('rating' in temp_hotel['hotel']):
                hotel_rating = temp_hotel['hotel']['rating']
            if ('address' in temp_hotel['hotel'] and 'lines' in temp_hotel['hotel']['address']):
                hotel_address = temp_hotel['hotel']['address']['lines'][0]
            if ('contact' in temp_hotel['hotel'] and 'phone' in temp_hotel['hotel']['contact']):
                hotel_contact = temp_hotel['hotel']['contact']['phone']
            if ('price' in temp_hotel['offers'] and 'total' in temp_hotel['offers']['price']):
                hotel_price = temp_hotel['offers']['price']['total']

            hotel_prase = hotel(name=hotel_name, unit=hotel_unit, rate=hotel_rating, price=hotel_price,
                                communication=hotel_contact, postcode= hotel_postcode, position=hotel_address)
            all_hotel.append(hotel_prase)
    return all_hotel[0]


if __name__ == '__main__':
    pass
    resp = get_hotel('Paris')
