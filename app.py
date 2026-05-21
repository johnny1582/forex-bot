from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "DQ2HOOSEVHP7MZ7R"

def get_price():

    try:

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

        series = data.get("Time Series FX (5min)")

        if not series:
            return None

        latest = list(series.values())[0]

        price = float(latest["4. close"])

        return price

    except Exception as e:

        print("ERROR:", e)

        return None

@app.route("/")
def home():

    price = get_price()

    signal = "WAIT"

    if price:

        if price > 1.10:
            signal = "BUY"

        else:
            signal = "SELL"

    return render_template(
        "index.html",
        price=price,
        signal=signal
    )

if __name__ == "__main__":
    app.run()
