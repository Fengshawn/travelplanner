from flask import Flask, render_template, request
import pdfkit
from Flight import get_flight
from Flight import retrive_flight_data
from Models import flight

app = Flask(__name__)
# init information
place_dict = {'beijing': 'PEK', '北京': 'PEK', 'Beijing': 'PEK', 'BEIJING': 'PEK', 'London': 'LHR', "伦敦": 'LHR',
              'london': 'LHR'}


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=["POST", "GET"])
def result():
    Airline_start = request.form.get('startplace')
    Airline_end = request.form.get('endplace')
    startday = request.form.get('startday')
    travellers = request.form.get('travellers')
    email = request.form.get('email')
    print(email)
    # here transfer into code
    Airline_start_code = str(place_dict[Airline_start])
    Airline_end_code = str(place_dict[Airline_end])
    startday = str(startday).strip()
    travellers = int(travellers)
    all_flight = retrive_flight_data(Airline_start_code, Airline_end_code, startday, travellers)
    return render_template("result.html", name=all_flight[0].name, time=all_flight[0].time
                           , price=all_flight[0].price, package=all_flight[0].package,
                           cabin=all_flight[0].cabin, details=all_flight[0].details)


if __name__ == '__main__':
    app.run()
