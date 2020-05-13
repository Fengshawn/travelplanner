from flask import Flask, render_template, request
from Flight import get_flight
from EmailSend import send_email
from hotel import get_hotel
from datetime import datetime, timedelta
from locations import get_location
from Activities import get_travel_line
from transportation import calculate_time_distance
from getPrice import get_price
import pdfkit
import os

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

    #Start Areej Part
    cabin = request.form.get('cabin')
    # this is cabin informaiton
    cabin = str(cabin).strip()
    # transfer into code
    # End Areej Part

    Airline_start_code = str(get_location(Airline_start))
    Airline_end_code = str(get_location(Airline_end))
    startday = str(startday).strip()
    travellers = int(travellers)

    # Start Areej Part
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
    checked_cats.append('zoo') if 'zoo' in request.form else None
    checked_cats.append('museum') if 'museum' in request.form else None


    # if user doesnt choose any options
    if len(checked_cats) == 0:
        checked_cats.append('art gallery')
        checked_cats.append('amusement park')
        checked_cats.append('tourist attraction')
        checked_cats.append('aquarium')
        checked_cats.append('shopping mall')
        checked_cats.append('zoo')
        checked_cats.append('museum')

    # calculate the days users will travel
    days_diff = datetime.strptime(str(endday).strip(), '%Y-%m-%d') - datetime.strptime(str(startday).strip(),
                                                                                       '%Y-%m-%d')
    dates_list = list()
    for day in range(0, days_diff.days):
        date = datetime.strptime(str(startday).strip(), '%Y-%m-%d') + timedelta(days=day)
        dates_list.append(date.strftime('%Y-%m-%d'))
    days_diff = days_diff
    # get user want travel days
    days = days_diff.days + 1

    all_flight = get_flight(Airline_start_code, Airline_end_code, startday, travellers, cabin)
    # get hotel data from here
    hotel_data = get_hotel(Airline_end, days)
    # get days activities
    restaurant_list, attraction_list = get_travel_line(Airline_end, days, checked_cats, 2)
    # get average transportation
    days_activities = calculate_time_distance(hotel_data, attraction_list, restaurant_list, days)
    budget = get_price(hotel_data, all_flight, [activity for activity in days_activities if activity.type in 'transportation'])
    html = render_template("result.html",
                           name=all_flight['aircraft_code'],
                           cabin=cabin.title().replace("_", " "),
                           dtime=all_flight['departure_dtime'],
                           atime=all_flight['arrival_dtime'],
                           arr_airport=all_flight['arrival_airport'],
                           dep_airport=all_flight['departure_airport'],
                           price=all_flight['price'],
                           duration=all_flight['duration'],
                           hotel_data=hotel_data,
                           days_diff=int(days),
                           days_activities=days_activities,
                           city=Airline_end,
                           dates=dates_list,
                           budget=budget
                           )
    # Added the function to calculate time price and distance

    # Depend on your system uncomment and comment in order to make pdf to be sent.
    #try:                                                                               # Windows
        # Save the PDF to local directory if the user wants to receive it via email
        #path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'          # Windows
        #config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)                     # Windows
    css = 'static/css/resStyle.css'
    try:
        os.remove('static/temp/plan.pdf')  # Delete the previous PDF document
    except FileNotFoundError:
        pass
    #pdfkit.from_string(html, 'static/temp/plan.pdf', configuration=config, css=css) # Windows
    pdf_path = f"{os.path.dirname(__file__)}{os.sep}static/temp/plan.pdf"            # MAC
    pdfkit.from_string(html, pdf_path, css=css)
    #except OSError:                                                                #Windows
     #   pass                                                                       # Windows
    return html


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
# End Areej Part