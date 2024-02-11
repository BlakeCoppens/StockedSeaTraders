from flask import Flask, render_template, request
from stockInfo import *
from waitress import serve
app = Flask(__name__)

@app.route('/')
@app.route('/index')


def index():
    return render_template('index.html')

@app.route('/stockInfo')
def getStockData():
    stock = request.args.get('stockName')
    response = findStockInfo(stock)
    return render_template(
        "stock.html",
        title = stock,
        status = response
    )

if __name__ == "__main__":
    serve(app, host = "0.0.0.0", port = 8000)