from flask import Flask,request
from main import flight
from webscraber import scraping


app  = Flask(__name__)

@app.route("/tt")
def hi():
    myfligh = flight("ankara", "dusseldorf", "one way", "30.03.2023", False)
    urls = myfligh.searchFlight()
    data = scraping(urls)

    return data

@app.route("/<username>")
def showname(username):
    print(username)
    return username


@app.route("/data",methods=['GET','POST'])
def getData():
    if request.method == 'POST':
        print(request.get_json())
        data = request.get_json()
        myfligh = flight(data['from'], data['goTo'], data['way'], data['date'], data['returnDate'])
        urls = myfligh.searchFlight()
        datas = scraping(urls)
        print(datas)
        return datas
    if request.method == 'GET':
        return "hallo man"
    return -1





if __name__ == '__main__':
    app.run(debug=True, port=8000)