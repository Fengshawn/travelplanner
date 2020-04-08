from amadeus import Client, ResponseError
from Models import flight

amadeus = Client(
    client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
    client_secret='IWBwclckwNgBKNWr'
)


# # get All flight Information
# def get_flight(start_place_code, end_place_code, start_data, traveller):
#     try:
#         response = amadeus.shopping.flight_offers_search.get(
#             originLocationCode=start_place_code,
#             destinationLocationCode=end_place_code,
#             departureDate=start_data,
#             adults=traveller)
#         return response
#     except ResponseError as error:
#         print(error)


# init information
start_place_code = 'MAN'
end_place_code = 'PEK'
start_data = '2020-04-20'
traveller = 1


# test information PEK  LHR  2020-03-29    2020-03-31
def retrive_flight_data(start_place_code, end_place_code, start_data, traveller):
    # store flight information
    all_flight_list = list()
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode=start_place_code,
        destinationLocationCode=end_place_code,
        departureDate=start_data,
        adults=traveller)
    temp_response = response.data
    # Retrieved All flight
    flight_all = len(temp_response)
    # print(temp_response)
    for i in range(flight_all):
        # flight name information
        temp_name = temp_response[i]['validatingAirlineCodes'][0]
        # stop times
        temp_stop_times = len(temp_response[i]['itineraries'][0]['segments'])
        # total time to destination
        temp_total_time = temp_response[i]['itineraries'][0]['duration']
        temp_total_time = str(temp_total_time).replace('PT', "")
        temp_total_time = str(temp_total_time).replace('H', "小时")
        temp_total_time = str(temp_total_time).replace('M', "分钟")
        # total cost flight
        total_cost = (temp_response[i])['price']['total']
        # cabin information
        temp_cabin = temp_response[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['cabin']
        # pacakage information
        temp_package = 0
        if ('weight' in temp_response[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']):
            temp_package = temp_response[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags'][
                'weight']
        elif (temp_response[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']['quantity']):
            temp_package = 46

        temp_details = ''
        flight_details = list()
        flight_details.clear()
        # this is the details of

        for j in range(len(temp_response[i]['itineraries'][0]['segments'])):
            # --------------------departure information----------------------------------
            # flight_company information
            company_flight = temp_response[i]['itineraries'][0]['segments'][j]['carrierCode']

            # company_flight_number
            flight_number = temp_response[i]['itineraries'][0]['segments'][j]['aircraft']['code']
            # iata_code_departure
            iata_code_departure = temp_response[i]['itineraries'][0]['segments'][j]['departure']['iataCode']
            # start_time
            start_time = temp_response[i]['itineraries'][0]['segments'][j]['departure']['at']
            # start_terminal
            start_terminal = 1
            if ('terminal' in temp_response[i]['itineraries'][0]['segments'][j]['departure']):
                # terminal information
                start_terminal = temp_response[i]['itineraries'][0]['segments'][j]['departure']['terminal']
            # ----------------------------------arrival information---------------------------
            # iata_code_arrival
            iata_code_arrival = temp_response[i]['itineraries'][0]['segments'][j]['arrival']['iataCode']
            # arrive_time
            arrive_time = temp_response[i]['itineraries'][0]['segments'][j]['arrival']['at']
            # arrival_terminal
            arrival_terminal = 1
            if ('terminal' in temp_response[i]['itineraries'][0]['segments'][j]['arrival']):
                # terminal information
                arrival_terminal = temp_response[i]['itineraries'][0]['segments'][j]['arrival']['terminal']
            temp_details = str(company_flight) + str(
                flight_number), iata_code_departure, start_time, 'Terminal: ' + str(
                start_terminal), iata_code_arrival, arrive_time, 'Terminal: ' + str(arrival_terminal)
            flight_details.append(temp_details)

        temp_flight = flight(temp_name, temp_total_time, total_cost, temp_stop_times, temp_package,
                             details=flight_details,
                             cabin=temp_cabin)

        all_flight_list.append(temp_flight)
    return all_flight_list


flight_list = retrive_flight_data(start_place_code, end_place_code, start_data, traveller)
for i in flight_list:
    print(i.cabin)
