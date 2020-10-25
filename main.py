from flask import Flask, render_template, request, jsonify
from location import getLocations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locations', methods=('GET',))
def test():
    if not request.data:
        return "No coordinates found!"
    # return (request.json['coordinates'])
    return  jsonify(getLocations(request.json['coordinates']))

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)