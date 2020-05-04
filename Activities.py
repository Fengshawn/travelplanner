"""
@author:Areej
@file:google_places.py

"""
import random
import googlemaps
import time
from opencage.geocoder import OpenCageGeocode
from Models import restaurant
from Models import attraction


# 2 activities and 1 restaurant per day


def get_attraction(start_place, selected_categories):
    """

    :param start_place: City find places in
    :param selected_categories: selected categories except for the restaurants
    :return:
    """
    data = []
    # auto select number of days

    category_ref_dict = {
        "art gallery": "art_gallery",
        "tourist attraction": "tourist_attraction",
        "amusement park": "amusement_park",
        "aquarium": "aquarium",
        "shopping mall": "shopping_mall",
        "zoo": "zoo",
        "museum": "museum"
    }

    if (len(selected_categories) == 0):
        selected_categories.append("art gallery")
        selected_categories.append("tourist attraction")
        selected_categories.append("shopping mall")
        selected_categories.append("aquarium")
        selected_categories.append("amusement park")
        selected_categories.append("zoo")
        selected_categories.append("museum")

    # deal with categories user selected
    params_cat = [category_ref_dict[category] for category in selected_categories]
    print(params_cat)
    # key need to be change
    key = "25cff282b29f43b9ac3aad454f1945a6"
    geocoder = OpenCageGeocode(key)  # Gecoding Service to get coordinates of city
    result = geocoder.geocode(start_place, no_annotations='1')  # Gecoding Service API key
    longitude = result[0]['geometry']['lng']  # Parsing Latitude
    latitude = result[0]['geometry']['lat']  # Parsing Longitude
    gmaps = googlemaps.Client(key='AIzaSyDUu2EVWYs1E5Wv7xuaJGZTCBqeDMXeu4U')

    """
    1.here need sometime to check where your api is okay 
    2.then select 3 pages(if here contain 3 pages) can be more 
    3.then store into related class
    4.use all_attraction to store attraction information
    """
    all_attraction = []

    for type in params_cat:
        response = gmaps.places_nearby(location=[latitude, longitude], radius=10000, type=type)
        attraction_type = type
        attraction_address = 'null'
        attraction_name = 'null'
        attraction_rating = 'null'
        attraction_latitude = 0
        attraction_longitude = 0
        for i in range(3):
            # use temp_response to store response
            temp_response = response
            # parse information
            print(temp_response)
            attraction_number = len(temp_response['results'])
            if (attraction_number >= 15):
                for temp_attraction in temp_response['results'][0:15]:
                    if ('geometry' in temp_attraction):
                        attraction_latitude = temp_attraction['geometry']['location']['lat']
                        attraction_longitude = temp_attraction['geometry']['location']['lng']
                    if ('rating' in temp_attraction):
                        attraction_rating = temp_attraction['rating']
                    if ('name' in temp_attraction):
                        attraction_name = temp_attraction['name']
                    if ('vicinity' in temp_attraction):
                        attraction_address = temp_attraction['vicinity']
                    attraction_prase = attraction(address=attraction_address, longitude=attraction_longitude,
                                                  latitude=attraction_latitude, name=attraction_name,
                                                  rating=attraction_rating, type=attraction_type)
                    all_attraction.append(attraction_prase)
            elif (attraction_number < 15):
                for temp_attraction in temp_response['results']:
                    if ('geometry' in temp_attraction):
                        attraction_latitude = temp_attraction['geometry']['location']['lat']
                        attraction_longitude = temp_attraction['geometry']['location']['lng']
                    if ('rating' in temp_attraction):
                        attraction_rating = temp_attraction['rating']
                    if ('name' in temp_attraction):
                        attraction_name = temp_attraction['name']
                    if ('vicinity' in temp_attraction):
                        attraction_address = temp_attraction['vicinity']
                    attraction_prase = attraction(address=attraction_address, longitude=attraction_longitude,
                                                  latitude=attraction_latitude, name=attraction_name,
                                                  rating=attraction_rating, type=attraction_type)
                    all_attraction.append(attraction_prase)
            # check whether is contain next_page_token
            if ('next_page_token' in temp_response):
                page_token = temp_response['next_page_token']
                # need time to check
                time.sleep(2)
                response = gmaps.places_nearby(location=[latitude, longitude], radius=10000, type='restaurant',
                                               page_token=page_token)
                temp_response = response
            else:
                break

    return all_attraction


def get_restaurant(start_place, type='restaurant'):
    # key need to be change
    key = "25cff282b29f43b9ac3aad454f1945a6"
    geocoder = OpenCageGeocode(key)  # Gecoding Service to get coordinates of city
    result = geocoder.geocode(start_place, no_annotations='1')  # Gecoding Service API key
    longitude = result[0]['geometry']['lng']  # Parsing Latitude
    latitude = result[0]['geometry']['lat']  # Parsing Longitude
    gmaps = googlemaps.Client(key='AIzaSyDVs1QGncUOixJm3-ODbkg_OZ4THdknzwI')

    """
    1.here need sometime to check where your api is okay 
    2.then select 3 pages(if here contain 3 pages)
    3.then store into related class
    4.use all_hotel to store restaurant information
    """
    response = gmaps.places_nearby(location=[latitude, longitude], radius=10000, type='restaurant')
    all_restaurant = []
    restaurant_address = 'null'
    restaurant_name = 'null'
    restaurant_rating = 'null'
    restaurant_latitude = 0
    restaurant_longitude = 0
    restaurant_type = 'restaurant'
    for i in range(3):
        # use temp_response to store response
        temp_response = response
        # parse information
        # print(temp_response)
        restaurant_number = len(temp_response['results'])
        if (restaurant_number >= 3):
            for temp_restaurant in temp_response['results'][0:3]:
                if ('geometry' in temp_restaurant):
                    restaurant_latitude = temp_restaurant['geometry']['location']['lat']
                    restaurant_longitude = temp_restaurant['geometry']['location']['lng']
                if ('rating' in temp_restaurant):
                    restaurant_rating = temp_restaurant['rating']
                if ('name' in temp_restaurant):
                    restaurant_name = temp_restaurant['name']
                if ('vicinity' in temp_restaurant):
                    restaurant_address = temp_restaurant['vicinity']
                restaurant_prase = restaurant(address=restaurant_address, longitude=restaurant_longitude,
                                              latitude=restaurant_latitude, name=restaurant_name,
                                              rating=restaurant_rating, type=restaurant_type)
                all_restaurant.append(restaurant_prase)
        elif (restaurant_number < 3):
            for temp_restaurant in temp_response['result']:
                if ('geometry' in temp_restaurant):
                    restaurant_latitude = temp_restaurant['geometry']['location']['lat']
                    restaurant_longitude = temp_restaurant['geometry']['location']['lng']
                if ('rating' in temp_restaurant):
                    restaurant_rating = temp_restaurant['rating']
                if ('name' in temp_restaurant):
                    restaurant_name = temp_restaurant['name']
                if ('vicinity' in temp_restaurant):
                    restaurant_address = temp_restaurant['vicinity']
                restaurant_prase = restaurant(address=restaurant_address, longitude=restaurant_longitude,
                                              latitude=restaurant_latitude, name=restaurant_name,
                                              rating=restaurant_rating, type=restaurant_type)
                all_restaurant.append(restaurant_prase)
        # check whether is contain next_page_token
        if ('next_page_token' in temp_response):
            page_token = temp_response['next_page_token']
            # need time to check
            time.sleep(2)
            response = gmaps.places_nearby(location=[latitude, longitude], radius=10000, type='restaurant',
                                           page_token=page_token)
            temp_response = response
        else:
            break

    return all_restaurant


def get_travel_line(start_place, days, selected_categories, activity_threshold):
    """
    :param start_place: City find places in
    :param days: number of days for the stay
    :param selected_categories: selected categories except for the restaurants
    :param activity_threshold: number of categories per day except for the restaurant
    :return: attractions list  && restaurant we choose
    """
    restaurant_list = get_restaurant(start_place, type='restaurant')
    attraction_list = get_attraction(start_place, selected_categories)
    restaurant_choose = []
    attraction_choose = []
    # get all attraction number
    attraction_list_all_number = len(attraction_list)
    print("attraction_list_all_number", attraction_list_all_number)
    # get all what people we need
    travel_all_number = activity_threshold * days
    # random generate
    list_number = get_various_number(travel_all_number, attraction_list_all_number)
    list_number_restaurant = len(restaurant_list)

    if (travel_all_number <= attraction_list_all_number):
        for i in list_number:
            print(i)
            attraction_choose.append(attraction_list[i])
    elif (travel_all_number > attraction_list_all_number):
        try:
            print("no more related place")
        except:
            SystemError
        # out of index will lead to revisite

    if (days <= list_number_restaurant):
        for i in range(days):
            restaurant_choose.append(restaurant_list[i])
    elif (days > list_number_restaurant):
        restaurant_choose.append(restaurant_list)

    return restaurant_choose, attraction_choose


def get_various_number(times, max_number):
    # list_number = random.sample(range(0, max_number), times)
    list_number = set()
    # for i in range(times):
    #     list_number.add(random.randint(0, max_number - 1))
    if (max_number >= times):
        while (True):
            if (len(list_number) <= times):
                list_number.add(random.randint(0, max_number - 1))
            else:
                break
    elif (max_number < times):
        for i in range(max_number):
            list_number.add(i)
    list_number = list(list_number)
    return list_number


if __name__ == '__main__':
    # ress = get_restaurant('London', "restaurant")
    resp, resp2 = get_travel_line('London', 1, ["art gallery"], 2)
    print(resp[0].latitude)
    print(resp[0].longitude)
