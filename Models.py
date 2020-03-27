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
