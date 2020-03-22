"""
@author:ZRM
@file:Test_Algorithm.py
@time:2020/03/23
"""
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
    client_secret='IWBwclckwNgBKNWr'
)


class flight():
    def __init__(self, name, time, price, stop_times, package, details, cabin):
        self.name = name
        self.time = time
        self.price = price
        self.stop_times = stop_times
        self.package = package
        self.details = details
        self.cabin = cabin


def get_flight(start_place_code, end_place_code, start_data, traveller):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=start_place_code,
            destinationLocationCode=end_place_code,
            departureDate=start_data,
            adults=traveller)
        return response
    except ResponseError as error:
        print(error)


all_flight = list()
Airline_start_code = str('PEK')
Airline_end_code = str('LHR')
startday = str('2020-07-01').strip()
travellers = int(1)
response = get_flight(Airline_start_code, Airline_end_code, startday, travellers)

for i in range(len(response.data)):
    # 一共有N站需要停靠
    # print("停靠站次数", len(response.data[i]['itineraries'][0]['segments']))
    temp_stop_times = len(response.data[i]['itineraries'][0]['segments'])
    # 一共需要飞多久
    tempxx = response.data[i]['itineraries'][0]['duration']
    tempxx = str(tempxx).replace('PT', "")
    tempxx = str(tempxx).replace('H', "hour")
    tempxx = str(tempxx).replace('M', "minutes")
    temp_time = tempxx
    # print("一共飞行时长", tempxx)
    # 一共要多少钱单位是EUR
    # print("价格是EUR:", (response.data[i])['price']['total'])
    temp_price = (response.data[i])['price']['total']
    # 仓位信息
    # print("舱位信息", response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['cabin'])
    temp_cabin = response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['cabin']
    # 行李额
    if ('weight' in response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']):
        temp_package = response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags'][
                           'weight'], "KG"

        # print("行李额度",response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']['weight'],"KG")
    elif (response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']['quantity']):
        temp_package = '46'
        # print("行李额度", 46, "KG")

    # details for flight
    temp_name = response.data[0]['validatingAirlineCodes'][0]
    for i in range(len(response.data[0]['itineraries'][0]['segments'])):

        # print("飞机信息：", response.data[0]['validatingAirlineCodes'][0],
        #       response.data[0]['itineraries'][0]['segments'][i]['aircraft']['code'])
        if ('terminal' in response.data[0]['itineraries'][0]['segments'][i]['departure']):
            #print("在这里转机或者出发Terminal：", response.data[0]['itineraries'][0]['segments'][i]['departure']['terminal'])
            temp_details = response.data[0]['itineraries'][0]['segments'][i]['departure']['at'] + "From:", \
                           response.data[0]['itineraries'][0]['segments'][i]['departure']['terminal'], "---->"
        #print("在时间出发", response.data[0]['itineraries'][0]['segments'][i]['departure']['at'])

       #print("到达第", i + 1, "站")
        # print("飞机信息：", response.data[0]['validatingAirlineCodes'][0])
        #print(response.data[0]['itineraries'][0]['segments'][i]['arrival']['iataCode'])
        if ('terminal' in response.data[0]['itineraries'][0]['segments'][i]['departure']):
            temp_details += "---->", response.data[0]['itineraries'][0]['segments'][i]['arrival']['iataCode'], \
                            response.data[0]['itineraries'][0]['segments'][i]['arrival']['at'] + "to", \
                            response.data[0]['itineraries'][0]['segments'][i]['departure']['terminal']
        #     print("在这里转机或者出发Terminal", response.data[0]['itineraries'][0]['segments'][i]['departure']['terminal'])
        # print("到达时间：", response.data[0]['itineraries'][0]['segments'][i]['arrival']['at'])

    flight1 = flight(temp_name, temp_time, temp_price, temp_stop_times, temp_package, temp_details, temp_cabin)
    all_flight.append(flight1)
print(all_flight[0].price)
print(all_flight[0].stop_times)
print(all_flight[0].cabin)
print(all_flight[0].package)
print(all_flight[0].time)