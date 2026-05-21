from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "DQ2HOOSEVHP7MZ7R"

def get_price():

    url = (
        "https://www.alphavantage.co/query?"
        "function=FX_INTRADAY"
        "&from_symbol=EUR"
        "&to_symbol=USD"
        "&interval=5min"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    latest = list(
        data["Time Series FX (5min)"].values()
    )[0]

    price = float(latest["4. close"])

    return price

@app.route("/")
def home():

    price = get_price()

    signal = "WAIT"

    if price > 1.10:
        signal = "BUY"

    elif price < 1.10:
        signal = "SELL"

    return render_template(
        "index.html",
        price=round(price, 5),
        signal=signal
    )

if __name__ == "__main__":

    if __name__ == "__main__":
    app.run()