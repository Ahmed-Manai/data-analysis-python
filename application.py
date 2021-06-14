import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template

application = Flask(__name__)


@application.route("/")
def index():
    return render_template("index.html")


def generate_random_data():
    json_data = json.dumps(
        {
            "time": [1,2,3,4,5],
            "value": [6,7,8,9,10]
        }
    )
    yield f"data:{json_data}\n\n"

@application.route("/chart-data")
def chart_data():
    return Response(generate_random_data(), mimetype="text/event-stream")


if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True, threaded=True)
