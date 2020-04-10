"""
@author:Areej
@file:locations.py

"""
import pandas



def get_location(city):
    """
    This function creates the IATA city code from the data
    :param city: city name
    :return: city IATA code
    """
    csv = pandas.read_csv("static/images/IATA_codes.csv")

    for row in zip(csv['Location'], csv['Airport']):
        if city.lower() == row[0].lower():
            return row[1].upper()


if __name__ == '__main__':
    resp = get_location('beijing')
    print(resp)