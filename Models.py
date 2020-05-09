class hotel():
    def __init__(self, name, price, position, communication, unit, rate,postcode):
        self.name = name
        self.price = price
        self.position = position
        self.communication = communication
        self.unit = unit
        self.rate = rate
        self.postcode = postcode


class flight():
    def __init__(self, name, time, price, stop_times, package, details, cabin):
        self.name = name
        self.time = time
        self.price = price
        self.stop_times = stop_times
        self.package = package
        self.details = details
        self.cabin = cabin



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


class transportation():
    def __init__(self, type, time, money):
        self.type = type
        self.time = time
        self.money = money
