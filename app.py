from flask import Flask, render_template, request
import pdfkit
#config = pdfkit.configuration(wkhtmltopdf='D:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
app = Flask(__name__)


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
    return render_template("line.html", destination= destination,
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
