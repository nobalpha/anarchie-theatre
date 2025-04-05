from flask import Flask, render_template
import json
import datetime

app = Flask(__name__, static_folder="./static",
            static_url_path="/", template_folder="./templates")

DB_file = "./comments.json"


@app.route('/')
def hello():
    return render_template('index.html', DB=read_json(DB_file)["comments"])


@app.route('/flush/<passw>')
def flushDB(passw):
    if passw == "1":
        write_json(DB_file, {"comments": []})
    return render_template("index.html")


@app.template_filter('millis')
def timectime(ms):
    return datetime.datetime.fromtimestamp(int(ms)/1000.0)


def write_json(path, json_data):
    with open(path, 'w') as file_out:
        json.dump(json_data, file_out)


def read_json(path):
    with open(path) as file_in:
        return json.load(file_in)


app.run("localhost", 443, debug=False)
