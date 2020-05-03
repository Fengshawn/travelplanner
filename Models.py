"""
@author:ZRM
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
    def __init__(self, name, price, position, communication, latitude, longitude, unit, rate):
        self.name = name
        self.price = price
        self.position = position
        self.communication = communication
        self.latitude = latitude
        self.longitude = longitude
        self.unit = unit
        self.rate = rate


class attraction():
    def __init__(self, name, type, rating, latitude, longitude, address):
        self.name = name
        self.type = type
        self.rating = rating
        self.latitude = latitude
        self.longitude = longitude
        self.address = address


class restaurant():
    def __init__(self, name, rating, latitude, longitude, address, type):
        self.name = name
        self.rating = rating
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
        self.type = type


# class transportation():
# #     def __init__(self, type, time, money):
# #         self.type = type
# #         self.time = time
# #         self.money = money

class transportation():
    def __init__(self,  total_distance, total_time, steps_distance, steps_time, steps_instruction,transit_type):
        self.total_distance = total_distance
        self.total_time = total_time
        self.steps_distance = steps_distance
        self.steps_time = steps_time
        self.steps_instruction = steps_instruction
        self.transit_type = transit_type