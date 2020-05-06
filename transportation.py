import googlemaps
from datetime import datetime
from humanfriendly import format_timespan, round_number
from Models import transportation
from hotel import get_hotel
from Activities import get_travel_line


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


def calculate_time_distance(hotel, places_list, restaurants_list, days):
    """

    :param hotel: Hotel Object
    :param places_list: List of Place Objects
    :param restaurants_list: List of Restaurants
    :return:
    """
    places_list = [places_list[i:i+days] for i in range(0, len(places_list), days)]  # create sub-lists for days


    transportaion_list = []
    gmaps = googlemaps.Client(key='AIzaSyDUu2EVWYs1E5Wv7xuaJGZTCBqeDMXeu4U')
    #
    for index, places in enumerate(places_list):
        day_list = []
        line_sequence = [hotel, places[0], restaurants_list[index]] + places[1:] if len(places) > 1 else []
        for sindex, sequence in enumerate(line_sequence):
            total_distance = 0
            total_duration = 0
            total_price = 0
            if sindex < len(line_sequence) - 1:
                directions_result = gmaps.directions(origin=[sequence.latitude, sequence.longitude],
                                                     destination=[line_sequence[sindex+1].latitude,
                                                                  line_sequence[sindex+1].longitude],
                                                     mode="transit")
                if directions_result:
                    for path in directions_result[0]['legs']:
                        total_distance += path['distance']['value']
                        total_duration += path['duration']['value']
                        total_price += path['fare']['value'] if 'fare' in path.keys() else 0
            if total_distance:
                total_distance = f"{round_number(total_distance/1000)} KM"
                total_duration = format_timespan(total_duration)
                total_price = f"{total_price} GBP" if total_price else "N/A"
                day_list.append([total_distance, total_duration, total_price])
        transportaion_list.append(day_list)
    transportaion_list.remove([])
    return transportaion_list


if __name__ == '__main__':

    hotel = get_hotel('London')
    restaurants_list, places_list = get_travel_line('London', 2, ["art gallery"], 2)
    response = calculate_time_distance(hotel, places_list, restaurants_list, 2)
    print("Done!")

