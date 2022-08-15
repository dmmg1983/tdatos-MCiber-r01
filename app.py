from flask import Flask, Response, request

import json

from yahoo import search_in_yahoo_finance
import pprint
app = Flask(__name__)


@app.route("/")
def main():
    return "Hola Mundo"

@app.route("/api/search/")
def search():
    ticker = request.args.get("params")
    financial_info = search_in_yahoo_finance(ticker=ticker)
    return Response(json.dumps({
        "ticker": ticker,
        "longname": financial_info["quotes"][0]["longname"],
        "shortname": financial_info["quotes"][0]["shortname"],
        "symbol": financial_info["quotes"][0]["symbol"],
        "exchange": financial_info["quotes"][0]["exchange"],
        "exchDisp": financial_info["quotes"][0]["exchDisp"],
        "sector": financial_info["quotes"][0]["sector"],
        "industry": financial_info["quotes"][0]["industry"],
        "score": financial_info["quotes"][0]["score"],
        "isYahooFinance": financial_info["quotes"][0]["isYahooFinance"]
    }), status=200, mimetype="application/json")
@app.route ("/api/current-price")
def current_price():
    return "<p>Hello, current price!</p>"
