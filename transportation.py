import googlemaps
from datetime import datetime

from Activities import get_travel_line
from Models import transportation
from hotel import get_hotel

gmaps = googlemaps.Client(key='AIzaSyDVs1QGncUOixJm3-ODbkg_OZ4THdknzwI')

# Request directions via public transit
# now = datetime.now()
#
# directions_result = gmaps.directions([51.50732, -0.13239],
#                                      [51.5104568, -0.1210495],
#                                      mode="walking")


def get_transportation(origin, destination):
    # print(len(destination), "destination")
    all_transportation = []
    directions_result = gmaps.directions([origin.latitude, origin.longitude],
                                         [destination.latitude, destination.longitude],
                                         mode="transit")

    transportation_distance = directions_result[0]['legs'][0]['distance']['text'] # total distance
    transportation_time = directions_result[0]['legs'][0]['duration']['text']  # total time cost

    transportation_type = []  # from origin to destination may contains more than 1 type for transportation
    steps_distance = []  # distance for each step
    steps_time = []  # time cost for each step
    steps_instruction = []  # html instruction for each step

    steps_num = len(directions_result[0]['legs'][0]['steps'])  # the number of steps from startplace to destination

    for i in range(steps_num):  # iterate each step
        steps_instruction += [directions_result[0]['legs'][0]['steps'][i]['html_instructions']]
        steps_time += [directions_result[0]['legs'][0]['steps'][i]['duration']['text']]
        steps_distance += [directions_result[0]['legs'][0]['steps'][i]['distance']['text']]

        if 'transit_details' in directions_result[0]['legs'][0]['steps'][i]:
            transportation_type_temp = \
            directions_result[0]['legs'][0]['steps'][i]['transit_details']['line']['vehicle']['type']
        else:
            transportation_type_temp = 'Walking'

        transportation_type += [transportation_type_temp]

    temp_transportation = transportation(total_distance=transportation_distance,
                                         total_time=transportation_time,
                                         steps_distance=steps_distance,
                                         steps_time=steps_time,
                                         steps_instruction=steps_instruction,
                                         transit_type=transportation_type)

    all_transportation.append(temp_transportation)

    return all_transportation

