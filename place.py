"""
@author:Areej
@file:place.py

"""
from amadeus import Client
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
        "nightlife": "NIGHTLIFE",
        "shopping": "SHOPPING",
        "sights": "SIGHTS",
        "restaurant": "RESTAURANT",

    }
    params_cat = [category_ref_dict[category] for category in selected_categories]
    selected_cat_palces = {cat: [] for cat in params_cat}
    client = Client(
        client_id='YhUHykQeccgseWSSARlxtfIAzhdGgTM2',
        client_secret='IWBwclckwNgBKNWr'
    )
    key = "25cff282b29f43b9ac3aad454f1945a6" 
    geocoder = OpenCageGeocode(key)  # Gecoding Service to get coordinates of city
    result = geocoder.geocode(start_place, no_annotations='1')  # Gecoding Service API key
    longitude = result[0]['geometry']['lng']  # Parsing Latitude
    latitude = result[0]['geometry']['lat']  # Parsing Longitude
    for cat in params_cat:
        response = client.reference_data.locations.points_of_interest.get(latitude=latitude,   # Get location using AMADEUS POIs Endpoint
                                                                          longitude=longitude,
                                                                          category=cat)
        first_try = True
        while True:
            if first_try:
                [selected_cat_palces[cat].append(place) for place in response.data
                 if len(selected_cat_palces[cat]) <= days * 2]
                first_try = False
            if len(selected_cat_palces[cat]) <= days * 2:
                next_page = client.next(response)
                [selected_cat_palces[cat].append(place) for place in next_page.data
                 if len(selected_cat_palces[cat]) <= days * 2]
            else:
                break
    for day in range(days):
        row = []
        cats = [key for key in selected_cat_palces.keys() if key != "RESTAURANT"]
        cat_indices = [random.randint(0, len(cats)-1) for _ in range(activity_threshold)]
        for indx in cat_indices:
            random_data_index = random.randint(0, len(selected_cat_palces[cats[indx]])-1)  # Select random category
            item = selected_cat_palces[cats[indx]][random_data_index]
            selected_cat_palces[cats[indx]].pop(random_data_index)
            row.append((item['category'], item['name']))
        random_data_index = random.randint(0, len(selected_cat_palces["RESTAURANT"]) - 1)  # Select random restauranr
        cat_restaurant = selected_cat_palces["RESTAURANT"][random_data_index]
        row.append((cat_restaurant['category'], cat_restaurant['name']))
        selected_cat_palces["RESTAURANT"].pop(random_data_index)
        data.append((day+1, row))

    return data


if __name__ == '__main__':
    resp = get_place('London', 1, ['nightlife', 'sights'], 2)
    print("Done!")