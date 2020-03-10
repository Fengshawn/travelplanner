from amadeus import Client, ResponseError 

amadeus = Client(client_id = "YhUHykQeccgseWSSARlxtfIAzhdGgTM2", client_secret = "IWBwclckwNgBKNWr")
try:
    '''
    What are the best hotel offers during my trip to Madrid?
    '''
    # Get all offers in Madrid
    response = amadeus.shopping.hotel_offers.get(cityCode='LON')
    hotelid = response.data[0]['hotel']['hotelId']

    # 2nd endpoint - Select one hotel and query it for offers
    resp = amadeus.shopping.hotel_offers_by_hotel.get(hotelId = 'BGMILBGB')
    print(resp.data)

   # Confirm the availability of a specific offer 
    resp2 = amadeus.shopping.hotel_offer('XXX').get()

except ResponseError as error:
    print(error) 