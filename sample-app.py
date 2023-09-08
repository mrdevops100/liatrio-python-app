from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def get_timestamp():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "message" : "Automate all things..!!",
        "timestamp" : current_date
    }
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)