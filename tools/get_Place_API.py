"""
@author:ZRM
@file:get_Place_API.py
@time:2020/03/19
maps_key = 'AIzaSyDVs1QGncUOixJm3-ODbkg_OZ4THdknzwI'
"""
import json
import time
import urllib
from urllib.request import urlopen

import pprint
import googlemaps

import numpy as np

API_KEY = 'AIzaSyDVs1QGncUOixJm3-ODbkg_OZ4THdknzwI'
gmaps = googlemaps.Client(key=API_KEY)
all_place = gmaps.places_nearby(location=' 53.3841600, -1.4754100', radius=40000, open_now=False, type='cafe')
print(all_place)
tempMark = list()
for place in all_place['results']:
    if(('rating') in place):
        tempMark.append(place['rating'])
for i in tempMark:
    if i==0:
        tempMark.remove(i)
average=np.mean(tempMark)
for place in all_place['results']:
    #print(type(place))
    place_id = place['place_id']
    place_location = place['geometry']['location']
    place_name = place['name']
    place_types = place['types']
    place_photo = place['photos']
    place_scope = place['scope']
    place_rating = average
    if ('rating' in place):
        place_rating = place['rating']
    print("当前经纬度是", place_location)
    print("当前分数是", place_rating)
    print('建筑名字', place_name)
    print('当前类别', place_types)
    # print(place_scope)
    print("照片相关信息", place_photo[0]['html_attributions'])
    print("-------------------------------------------------")
    if __name__ == "__main__":
        pass
