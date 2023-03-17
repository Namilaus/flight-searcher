from flask import Flask,request
from main import flight
from webscraber import scraping


app  = Flask(__name__)

@app.route("/data",methods=['GET','POST'])
def getData():
    if request.method == 'POST':
        data = request.get_json()
        myfligh = flight(data['from'], data['goTo'], data['way'], data['date'], data['returnDate'])
        urls = myfligh.searchFlight()
        datas = scraping(urls)
        return datas
    if request.method == 'GET':
        return "hallo man there is nothing here just chill"
    return -1


if __name__ == '__main__':
    app.run(debug=True, port=8000)