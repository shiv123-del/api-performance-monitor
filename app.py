from flask import Flask, render_template, request
import requests
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        url = request.form["url"]

        try:
            start = time.time()

            response = requests.get(url)

            end = time.time()

            result = {
                "status_code": response.status_code,
                "response_time": round((end - start) * 1000, 2)
            }

        except Exception as e:

            result = {
                "status_code": "Error",
                "response_time": str(e)
            }

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)