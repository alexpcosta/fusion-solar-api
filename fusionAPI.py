from flask import Flask, request, jsonify
from fusionscrape import get_battery_status
import os
app = Flask(__name__)

#http://127.0.0.1:5000/battery_status?username=x&password=y

@app.route("/battery_status")
def battery_status():
    username = request.args.get("username")
    password = request.args.get("password")
    battery_status = {
        "soc_value": get_battery_status(username,password)
    }
    return jsonify(battery_status),200


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=os.environ.get("PORT"))