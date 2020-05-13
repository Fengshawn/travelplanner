"""
@author:Areej
@file:getPrice.py
"""

def get_price(hotel, flight, transportation):
    """
    To get the sum of the total budget for all activities, hotel, transportation, and flight
    :param hotel: Hotel Object
    :param flight: Flight Object
    :param transportation: List of transportation objects
    :return:
    """
    total_price = 0
    total_price += float(hotel.price)
    total_price += float(flight['price'].split(' ')[0])
    for transport in transportation:
        if transport.total_price not in "N/A":
            total_price += float(transport.total_price.split(' ')[0])
    return total_price
