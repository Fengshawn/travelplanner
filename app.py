from flask import Flask, render_template, request,Session
import sys
import pdfkit
config = pdfkit.configuration(wkhtmltopdf='D:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
app = Flask(__name__)
sys.path.append("../../..")


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/line", methods=["POST", "GET"])
def line():
    destination = request.form.get('destination')
    Airline_start = request.form.get('startplace')
    Airline_end = request.form.get('endplace')
    startday = request.form.get('startday')
    endday = request.form.get('endday')
    interest = request.form.getlist('interest')
    travellers = request.form.get('travellers')
    Session['destination']=destination
    Session['Airline_start']=Airline_start
    Session['Airline_end']=Airline_end
    Session['startday']=startday
    Session['endday']=endday
    Session['interest']=interest
    Session['travellers']=travellers
    return render_template("line.html", destination= Session['destination'],
                           startplace=Airline_start, endplace=Airline_end, travellers=travellers,
                           startday=startday, endday=endday,
                           interest=interest)


@app.route('/testpage', methods=["POST", "GET"])
def testpage():
    destination = request.form.get('destination')
    Airline_start = request.form.get('startplace')
    Airline_end = request.form.get('endplace')
    startday = request.form.get('startday')
    endday = request.form.get('endday')
    interest = request.form.getlist('interest')
    travellers = request.form.get('travellers')

    return render_template("testPage.html", destination=destination,
                           startplace=Airline_start, endplace=Airline_end, travellers=travellers,
                           startday=startday, endday=endday,
                           interest=interest)



if __name__ == '__main__':
    app.run()
