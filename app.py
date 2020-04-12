from flask import Flask, render_template, request
from Flight import retrive_flight_data
# from EmailSend import send_email
from QQSend import send_email
from hotel import get_hotel
from datetime import date, datetime
from locations import get_location
from Activities import get_travel_line
from transportation import get_london_static

app = Flask(__name__)


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("404.html")


@app.errorhandler(400)
def internal_server_error(e):
    return render_template("404.html")


@app.errorhandler(404)
def internal_server_error(e):
    return render_template("404.html")


@app.route('/success', methods=["POST", "GET"])
def success():
    email = request.form.get('email')
    if (email == ""):
        return render_template("email.html")
    else:
        try:
            send_email(email)
            return render_template("success.html")
        except:
            SystemError
    return render_template("success.html")


@app.route('/email', methods=["POST", "GET"])
def email():
    return render_template("email.html")


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route('/result', methods=["POST", "GET"])
def result():
    # get information from frontend
    Airline_start = request.form.get('startplace')
    Airline_end = request.form.get('endplace')
    startday = request.form.get('startday')
    endday = request.form.get('endday')
    travellers = request.form.get('travellers')

    # transfer into code
    Airline_start_code = str(get_location(Airline_start))
    Airline_end_code = str(get_location(Airline_end))
    startday = str(startday).strip()
    travellers = int(travellers)
    # init information user selected in frontend
    checked_cats = []
    checked_cats.append('art gallery') if 'art_gallery' in request.form else None  # check if sights are selected
    checked_cats.append(
        'amusement park') if 'amusement_park' in request.form else None  # check if nightlife are selected
    checked_cats.append(
        'tourist attraction') if 'tourist_attraction' in request.form else None  # check if shopping are selected
    checked_cats.append(
        'shopping mall') if 'shopping_mall' in request.form else None  # check if shopping are selected
    checked_cats.append('aquarium') if 'aquarium' in request.form else None

    # if user donot choose
    if len(checked_cats) == 0:
        checked_cats.append('art gallery')
        checked_cats.append('amusement park')
        checked_cats.append('tourist attraction')
        checked_cats.append('aquarium')
        checked_cats.append('shopping mall')
    print(checked_cats)

    # calculate the days users will travel
    days_diff = datetime.strptime(str(endday).strip(), '%Y-%m-%d') - datetime.strptime(str(startday).strip(),
                                                                                       '%Y-%m-%d')
    days_diff = days_diff
    # get user want travel days
    days = days_diff.days + 1

    all_flight = retrive_flight_data(Airline_start_code, Airline_end_code, startday, travellers)
    # get hotel data from here
    hotel_data = get_hotel(Airline_end)
    # get days activities
    restaurant_list, attraction_list = get_travel_line(Airline_end, days, checked_cats, 2)
    # get average transportation
    average_transportation = get_london_static()
    return render_template("result.html", name=all_flight[0].name, time=all_flight[0].time
                           , price=all_flight[0].price, package=all_flight[0].package,
                           cabin=all_flight[0].cabin, details=all_flight[0].details,
                           restaurant_list=restaurant_list,
                           hotel_data=hotel_data,
                           days_diff=int(days),
                           days_activities=attraction_list,
                           average_transportation=average_transportation
                           )


if __name__ == '__main__':
    app.run()
