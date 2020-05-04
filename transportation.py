import googlemaps
from datetime import datetime

from Activities import get_travel_line
from Models import transportation
from hotel import get_hotel

gmaps = googlemaps.Client(key='AIzaSyDVs1QGncUOixJm3-ODbkg_OZ4THdknzwI')

# Request directions via public transit
# now = datetime.now()


def get_transportation(origin, destination):

    all_transportation = []
    directions_result = gmaps.directions([origin.latitude, origin.longitude],
                                         [destination.latitude, destination.longitude],
                                         mode="transit")

    transportation_distance = directions_result[0]['legs'][0]['distance']['text']  # total distance
    transportation_time = directions_result[0]['legs'][0]['duration']['text']  # total time cost

    transportation_type = []  # from origin to destination may contains more than 1 type for transportation
    steps_distance = []  # distance for each step
    steps_time = []  # time cost for each step
    steps_instruction = []  # html instruction for each step
    transit_departure = [] # when step != 'walking', it would have departure stop and arrival stop
    transit_arrival = []

    steps_num = len(directions_result[0]['legs'][0]['steps'])  # the number of steps from startplace to destination

    for i in range(steps_num):  # iterate each step
        steps_instruction += [directions_result[0]['legs'][0]['steps'][i]['html_instructions']]
        steps_time += [directions_result[0]['legs'][0]['steps'][i]['duration']['text']]
        steps_distance += [directions_result[0]['legs'][0]['steps'][i]['distance']['text']]

        if 'transit_details' in directions_result[0]['legs'][0]['steps'][i]:
            transportation_type_temp = directions_result[0]['legs'][0]['steps'][i]['transit_details']['line']['vehicle']['name']
            transit_departure += [directions_result[0]['legs'][0]['steps'][i]['transit_details']['departure_stop']['name']]
            transit_arrival += [directions_result[0]['legs'][0]['steps'][i]['transit_details']['arrival_stop']['name']]
        else:
            transportation_type_temp = 'Walking'
            transit_departure += ['Null']
            transit_arrival += ['Null']

        transportation_type += [transportation_type_temp]

    all_transportation = transportation(total_distance=transportation_distance,
                                        total_time=transportation_time,
                                        steps_distance=steps_distance,
                                        steps_time=steps_time,
                                        steps_instruction=steps_instruction,
                                        transit_type=transportation_type,
                                        transit_departure=transit_departure,
                                        transit_arrival=transit_arrival)

    return all_transportation

#def get_all_transport(startplace_list,endplace_list):
