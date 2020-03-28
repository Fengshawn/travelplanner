from flask import Flask, render_template, request
import pdfkit
from Flight import get_flight
from Models import flight
import json
# config = pdfkit.configuration(wkhtmltopdf='D:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
app = Flask(__name__)

place_dict = {'beijing': 'PEK', '北京': 'PEK', 'Beijing': 'PEK', 'BEIJING': 'PEK', 'London': 'LHR', "伦敦": 'LHR',
              'london': 'LHR'}
@app.route('/')
def index():
    return render_template("index.html")


all_flight = list()
temp_name = 'test'
temp_price = 'test'
temp_time = 'test'
temp_package = 'test'
temp_stop_times = 'test'
temp_details = 'test'
temp_cabin = 'test'

@app.route('/result', methods=["POST", "GET"])
def result():
    Airline_start = request.form.get('startplace')
    Airline_end = request.form.get('endplace')
    startday = request.form.get('startday')
    travellers = request.form.get('travellers')
    # here transfer into code
    Airline_start_code = str(place_dict[Airline_start])
    Airline_end_code = str(place_dict[Airline_end])
    startday = str(startday).strip()
    travellers = int(travellers)
    response = get_flight(Airline_start_code, Airline_end_code, startday, travellers)

    for i in range(len(response.data)):
        # 一共有N站需要停靠
        # print("停靠站次数", len(response.data[i]['itineraries'][0]['segments']))
        temp_stop_times = len(response.data[i]['itineraries'][0]['segments'])
        # 一共需要飞多久
        tempxx = response.data[i]['itineraries'][0]['duration']
        tempxx = str(tempxx).replace('PT', "")
        tempxx = str(tempxx).replace('H', "hour")
        tempxx = str(tempxx).replace('M', "minutes")
        temp_time = tempxx
        # print("一共飞行时长", tempxx)
        # 一共要多少钱单位是EUR
        print("价格是EUR:", (response.data[i])['price']['total'])
        temp_price = (response.data[i])['price']['total']
        # 仓位信息
        print("舱位信息", response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['cabin'])
        temp_cabin = response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['cabin']
        # 行李额
        if ('weight' in response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']):
            temp_package = response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags'][
                               'weight'], "KG"

            # print("行李额度",response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']['weight'],"KG")
        elif (response.data[i]['travelerPricings'][0]['fareDetailsBySegment'][0]['includedCheckedBags']['quantity']):
            temp_package = '46'
            print("行李额度", 46, "KG")

        # details for flight
        temp_name = response.data[0]['validatingAirlineCodes'][0]
        for i in range(len(response.data[0]['itineraries'][0]['segments'])):

            print("飞机信息：", response.data[0]['validatingAirlineCodes'][0],
                  response.data[0]['itineraries'][0]['segments'][i]['aircraft']['code'])
            if ('terminal' in response.data[0]['itineraries'][0]['segments'][i]['departure']):
                print("在这里转机或者出发Terminal：", response.data[0]['itineraries'][0]['segments'][i]['departure']['terminal'])
                temp_details = response.data[0]['itineraries'][0]['segments'][i]['departure']['at'] + "From:", \
                               response.data[0]['itineraries'][0]['segments'][i]['departure']['terminal'], "---->"
            print("在时间出发", response.data[0]['itineraries'][0]['segments'][i]['departure']['at'])

            print("到达第", i + 1, "站")
            # print("飞机信息：", response.data[0]['validatingAirlineCodes'][0])
            print(response.data[0]['itineraries'][0]['segments'][i]['arrival']['iataCode'])
            if ('terminal' in response.data[0]['itineraries'][0]['segments'][i]['departure']):
                temp_details += "---->", response.data[0]['itineraries'][0]['segments'][i]['arrival']['iataCode'], \
                                response.data[0]['itineraries'][0]['segments'][i]['arrival']['at'] + "to", \
                                response.data[0]['itineraries'][0]['segments'][i]['departure']['terminal']
                print("在这里转机或者出发Terminal", response.data[0]['itineraries'][0]['segments'][i]['departure']['terminal'])
            print("到达时间：", response.data[0]['itineraries'][0]['segments'][i]['arrival']['at'])

        flight1 = flight(temp_name, temp_time, temp_price, temp_stop_times, temp_package, temp_details, temp_cabin)
        all_flight.append(flight1)

    return render_template("result.html", name=all_flight[0].name, time=all_flight[0].time
                           , price=all_flight[0].price, package=all_flight[0].package,
                           cabin=all_flight[0].cabin, details=all_flight[0].details)
# testInfo={}
# @app.route('/result', methods=['GET', 'POST'])  # 路由
# def test_post():
#     testInfo['name'] = 'xiaoliao'
#     testInfo['age'] = '28'
#     return json.dumps(testInfo)

if __name__ == '__main__':
    app.run()
