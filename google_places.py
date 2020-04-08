"""
@author:Areej
@file:google_places.py

"""
import googlemaps
from opencage.geocoder import OpenCageGeocode
import random


# 2 activities and 1 restaurant per day


def get_place(start_place, days, selected_categories, activity_threshold):
    """

    :param start_place: City find places in
    :param days: number of days for the stay
    :param selected_categories: selected categories except for the restaurants
    :param activity_threshold: number of categories per day except for the restaurant
    :return:
    """
    data = []
    selected_categories.append("restaurant")
    category_ref_dict = {
        "art gallery": "art_gallery",
        "tourist attraction": "tourist_attraction",
        "amusement park": "amusement_park",
        "restaurant": "restaurant",
        "aquarium": "aquarium"

    }
    params_cat = [category_ref_dict[category] for category in selected_categories]
    selected_cat_palces = {cat: [] for cat in params_cat}

    key = "25cff282b29f43b9ac3aad454f1945a6"  
    geocoder = OpenCageGeocode(key)  # Gecoding Service to get coordinates of city
    result = geocoder.geocode(start_place, no_annotations='1')  # Gecoding Service API key
    longitude = result[0]['geometry']['lng']  # Parsing Latitude
    latitude = result[0]['geometry']['lat']  # Parsing Longitude
    gmaps = googlemaps.Client(key='AIzaSyDVs1QGncUOixJm3-ODbkg_OZ4THdknzwI')

    for cat in params_cat:
        response = gmaps.places_nearby(location=[latitude, longitude], radius=10000, type=cat)
        first_try = True
        next_page_token = response['next_page_token']
        while True:
            if first_try:
                [selected_cat_palces[cat].append(place) for place in response['results']
                 if len(selected_cat_palces[cat]) <= days * 2]
                first_try = False
            if len(selected_cat_palces[cat]) <= days * 2:
                response = gmaps.places_nearby(location=[latitude, longitude], radius=10000, type=cat,
                                               next_page_token=next_page_token)
                next_page_token = response['next_page_token']
                [selected_cat_palces[cat].append(place) for place in response['results']
                 if len(selected_cat_palces[cat]) <= days * 2]
            else:
                break
    for day in range(days):  # iteration over the days
        row = []
        cats = [key for key in selected_cat_palces.keys() if key != "restaurant"]
        cat_indices = [random.randint(0, len(cats)-1) for _ in range(activity_threshold)]
        for indx in cat_indices:
            random_data_index = random.randint(0, len(selected_cat_palces[cats[indx]])-1)  # Select random category
            item = selected_cat_palces[cats[indx]][random_data_index]
            selected_cat_palces[cats[indx]].pop(random_data_index)
            category = cats[indx]
            name = item['name']
            rating = item['rating'] if 'rating' in item.keys() else "Not Rated"
            address = item['vicinity']
            row.append((category, name, rating, address))
        random_data_index = random.randint(0, len(selected_cat_palces["restaurant"]) - 1)  # Select random restaurant
        cat_restaurant = selected_cat_palces["restaurant"][random_data_index]
        category = "restaurant"
        name = cat_restaurant['name']
        rating = cat_restaurant['rating'] if 'rating' in cat_restaurant.keys() else "Not Rated"
        address = cat_restaurant['vicinity']
        row.append((category, name, rating, address))
        selected_cat_palces["restaurant"].pop(random_data_index)
        data.append((day+1, row))

    return data


if __name__ == '__main__':
    resp = get_place('London', 1, ['art gallery', 'tourist attraction'], 2)
    # resp = get_place_by_id('ChIJEYfH57cEdkgRuNeOk-nbgeo')
    print("Done!")