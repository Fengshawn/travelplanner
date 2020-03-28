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
    def __init__(self, name, price, facility, rating, communication):
        self.name = name
        self.price = price
        self.facility = facility
        self.rating = rating
        self.communication = communication


class attraction():
    def __init__(self, name, price, type, rating):
        self.name = name
        self.price = price
        self.type = type
        self.rating = rating
