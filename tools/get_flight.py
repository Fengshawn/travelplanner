from amadeus import Client, ResponseError

amadeus = Client(
    client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
    client_secret='IWBwclckwNgBKNWr'
)

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='SYD',
        destinationLocationCode='BKK',
        departureDate='2020-07-01',
        adults=1)

    for i in range(len(response.data[0]['itineraries'][0]['segments'])):
        print("飞机信息：", response.data[0]['validatingAirlineCodes'][0],
              response.data[0]['itineraries'][0]['segments'][i]['aircraft']['code'])
        if ('terminal' in response.data[0]['itineraries'][0]['segments'][i]['departure']):
            print("在这里转机或者出发Terminal：", response.data[0]['itineraries'][0]['segments'][i]['departure']['terminal'])
        print("在时间出发", response.data[0]['itineraries'][0]['segments'][i]['departure']['at'])

        print("到达第", i + 1, "站")
        #print("飞机信息：", response.data[0]['validatingAirlineCodes'][0])
        print(response.data[0]['itineraries'][0]['segments'][i]['arrival']['iataCode'])
        if ('terminal' in response.data[0]['itineraries'][0]['segments'][i]['departure']):
            print("在这里转机或者出发Terminal", response.data[0]['itineraries'][0]['segments'][i]['departure']['terminal'])
        print("到达时间：", response.data[0]['itineraries'][0]['segments'][i]['arrival']['at'])

    # for i in range(len(response.data)):
    #     # 一共有N站需要停靠
    #     print("第", i + 1, "站飞机")
    #     print("停靠站次数", len(response.data[i]['itineraries'][0]['segments']))
    #
    #     # 一共需要飞多久
    #     tempxx = response.data[i]['itineraries'][0]['duration']
    #     tempxx = str(tempxx).replace('PT', "")
    #     tempxx = str(tempxx).replace('H', "小时")
    #     tempxx = str(tempxx).replace('M', "分钟")
    #     print("一共飞行时长", tempxx)
    #     # 一共要多少钱单位是EUR
    #     print("价格是EUR:", (response.data[i])['price']['total'])
    #     # 仓位信息
    #     print("舱位信息", response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['cabin'])
    #     # 行李额
    #     if ('weight' in response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']):
    #         print("行李额度",
    #               response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']['weight'],
    #               "KG")
    #     elif (response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']['quantity']):
    #         print("行李额度", 46, "KG")
    #     print("---------------------------------------")
    #

except ResponseError as error:
    print(error)
