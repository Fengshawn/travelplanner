import googlemaps
from datetime import datetime

from Activities import get_travel_line
from Models import transportation
from hotel import get_hotel

gmaps = googlemaps.Client(key='AIzaSyDVs1QGncUOixJm3-ODbkg_OZ4THdknzwI')

# Request directions via public transit
now = datetime.now()

directions_result = gmaps.directions([51.50732, -0.13239],
                                     [51.5104568, -0.1210495],
                                     mode="walking")


def get_transportation(startplace, destination):
    # print(len(destination), "destination")
    all_transportation = []
    transportation_type = 'walking'
    transportation_money = 0
    transportation_time = 15
    transportation_distance = 1
    for temp_destination in destination:
        directions_result = gmaps.directions([startplace.latitude, startplace.longitude],
                                             [temp_destination.latitude, temp_destination.longitude],
                                             mode="walking")
        transportation_distance = directions_result[0]['legs'][0]['distance']['text']
        transportation_time = directions_result[0]['legs'][0]['duration']['text']
        temp_transportation = transportation(type=transportation_type, distance=transportation_distance,
                                             time=transportation_time, money=transportation_money,
                                             startplace=startplace.name, endplace=temp_destination.name)
        all_transportation.append(temp_transportation)

    return all_transportation


def get_london_static():
    all_transportation = []
    transportation_type = ['walking', 'bus', 'taxi']
    transportation_time = [25, 30, 15]
    transportation_cost = [0, 5, 15]
    transportation_0 = transportation(time=transportation_time[0], money=transportation_cost[0],
                                      type=transportation_type[0])
    transportation_1 = transportation(time=transportation_time[1], money=transportation_cost[1],
                                      type=transportation_type[1])
    transportation_2 = transportation(time=transportation_time[2], money=transportation_cost[2],
                                      type=transportation_type[2])
    all_transportation.append(transportation_0)
    all_transportation.append(transportation_1)
    all_transportation.append(transportation_2)
    return all_transportation

