from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

# Starting mock values
soil = 32
temperature = 28.4
humidity = 71
pump = True
threshold = 40


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/data")
def api_data():
    global soil, temperature, humidity, pump

    # Simulate realistic sensor changes
    if pump:
        soil += random.randint(1, 3)

        if soil >= 44:
            pump = False
    else:
        soil -= random.randint(0, 2)

        if soil < threshold:
            pump = True

    # Keep values realistic
    soil = max(25, min(60, soil))

    temperature += random.uniform(-0.2, 0.2)
    temperature = round(temperature, 1)

    humidity += random.uniform(-1, 1)
    humidity = round(max(50, min(75, humidity)), 1)

    if soil < threshold:
        condition = "DRY"
        irrigation = "REQUIRED"
    else:
        condition = "MOIST"
        irrigation = "NOT REQUIRED"

    return jsonify({
        "soil": soil,
        "temperature": temperature,
        "humidity": humidity,
        "pump": pump,
        "threshold": threshold,
        "condition": condition,
        "irrigation": irrigation,
        "connected": True
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )