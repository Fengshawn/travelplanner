import googlemaps
from datetime import datetime, timedelta
from humanfriendly import format_timespan, round_number
from Models import transportation
from hotel import get_hotel
from Activities import get_travel_line
from time import time
from Models import transportation


def calculate_time_distance(hotel, places_list, restaurants_list, days):
    """

    :param hotel: Hotel Object
    :param places_list: List of Place Objects
    :param restaurants_list: List of Restaurants
    :return:
    """
    places_days_list = []  # create sub-lists for days
    for day in range(0, days):
        places_days_list.append([activities for activities in places_list[(day+1 - 1) * 2:(day+1) * 2]])

    compiled_list = []
    gmaps = googlemaps.Client(key='AIzaSyDUu2EVWYs1E5Wv7xuaJGZTCBqeDMXeu4U')
    #
    for index, places in enumerate(places_days_list[:days]):
        if len(places) > 1:
            line_sequence = [hotel, places[0], restaurants_list[index]] + places[1:]
        else:
            line_sequence = [hotel, places[0], restaurants_list[index]]
        last_time = datetime(2020, 5, 10, 9, 0, 0)
        for sindex, sequence in enumerate(line_sequence):
            total_distance = 0
            total_duration = 0
            total_price = 0
            from_to = "N/A"
            try:
                if sindex < len(line_sequence)-1:
                    directions_result = gmaps.directions(origin=[sequence.latitude, sequence.longitude],
                                                         destination=[line_sequence[sindex+1].latitude,
                                                                      line_sequence[sindex+1].longitude],
                                                         mode="transit")
                    if directions_result:
                        for path in directions_result[0]['legs']:
                            total_distance += path['distance']['value']
                            total_duration += path['duration']['value']
                            total_price += path['fare']['value'] if 'fare' in path.keys() else 0
                    from_to = f"{sequence.name} To {line_sequence[sindex + 1].name}"
            except IndexError:
                pass

            if sequence.type == 'Restaurant':
                time_difference = last_time + timedelta(seconds=sequence.duration)
                time_range = f'{last_time.strftime("%I:%M %p")}-{time_difference.strftime("%I:%M %p")}'
                last_time = time_difference
                restaurants_list[index].time_range = time_range
                compiled_list.append(restaurants_list[index])
            elif sequence.type not in ('hotel', 'Restaurant'):
                time_difference = last_time + timedelta(seconds=sequence.duration)
                time_range = f'{last_time.strftime("%I:%M %p")}-{time_difference.strftime("%I:%M %p")}'
                last_time = time_difference
                place_idx = places_list.index(sequence)
                places_list[place_idx].time_range = time_range
                compiled_list.append(places_list[place_idx])

            time_difference = last_time + timedelta(seconds=total_duration)
            trs_time_range = f'{last_time.strftime("%I:%M %p")}-{time_difference.strftime("%I:%M %p")}'
            last_time = time_difference

            total_distance = f"{round_number(total_distance/1000)} KM"
            total_duration = format_timespan(total_duration)
            total_price = f"{total_price} GBP" if total_price else "N/A"

            transport = transportation(total_distance, total_duration, total_price, trs_time_range, from_to)

            if total_distance != '0 KM':
                compiled_list.append(transport)

    compiled_list.remove([]) if [] in compiled_list else None
    return compiled_list


if __name__ == '__main__':

    hotel = get_hotel('London', 2)
    restaurants_list, places_list = get_travel_line('London', 2, ["art gallery"], 2)
    response = calculate_time_distance(hotel, places_list, restaurants_list, 2)
    print("Done!")
