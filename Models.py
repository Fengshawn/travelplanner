"""
@author:Runmin Zhang&Yanghao Zhou & Areej
@file:Models.py
@time:2020/03/28
"""

class flight():
    def __init__(self, name, time, price, stop_times, package, details, cabin):
        self.name = name
        self.time = time
        self.price = price
        self.stop_times = stop_times
        self.package = package
        self.details = details
        self.cabin = cabin


class hotel():
    def __init__(self, name, price, position, communication, latitude, longitude, unit, rate, days):
        self.name = name
        self.price = str(float(price) * days)
        self.position = position
        self.communication = communication
        self.latitude = latitude
        self.longitude = longitude
        self.unit = unit
        self.rate = rate
        self.type = 'hotel'


class attraction():
    def __init__(self, name, type, rating, latitude, longitude, address, photo, time_range=None):
        self.name = name
        self.type = type.title().replace("_", " ")
        self.rating = rating
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
        self.duration = 3600*2
        self.time_range = time_range
        self.photo = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&maxheight=500&photoreference={ photo }&key=AIzaSyDUu2EVWYs1E5Wv7xuaJGZTCBqeDMXeu4U"


class restaurant():
    def __init__(self, name, rating, latitude, longitude, address, type, photo, time_range=None):
        self.name = name
        self.rating = rating
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
        self.type = type.title()
        self.duration = 3600
        self.time_range = time_range
        self.photo = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&maxheight=500&photoreference={ photo }&key=AIzaSyDUu2EVWYs1E5Wv7xuaJGZTCBqeDMXeu4U"


class transportation():
    def __init__(self, total_distance, total_duration, total_price, time_range, from_to):
        self.type = 'transportation'
        self.total_distance = total_distance
        self.total_duration = total_duration
        self.total_price = total_price
        self.time_range = time_range
        self.from_to = from_to

