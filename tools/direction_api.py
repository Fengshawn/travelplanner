import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDVs1QGncUOixJm3-ODbkg_OZ4THdknzwI')

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions([51.50732, -0.13239],
                                     [51.5104568, -0.1210495],
                                     mode="walking",
                                     departure_time=now)
print(directions_result)
