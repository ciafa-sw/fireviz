
import os, time
from flask import Flask, Response, render_template, jsonify
from geojson import Point, Feature, FeatureCollection, Polygon

app = Flask(__name__)
app.debug = True

#ACCESS_KEY = os.environ.get('MAPBOX_ACCESSKEY')
ACCESS_KEY = 'pk.eyJ1IjoiZGlvZ29hb3MiLCJhIjoiY2p6YmMydDM4MDA0YTNqbzB4Y2JuOWV6MyJ9.57byXweMGWHJztAUs_P2Cw'

global i
i = 0.0001

p0 = [-8.318497, 39.954263]
p1 = [-8.318497+0.0005, 39.954263]
p2 = [-8.318497+0.0005, 39.954263+0.005]
p3 = [-8.318497, 39.954263+0.005]


@app.route('/')
def index():
    return render_template('index2.html', ACCESS_KEY=ACCESS_KEY)


@app.route('/result')
def process():
    global i
    point = Point((-8.318497+i, 39.954263))
    i += 0.0001
    feature = Feature(geometry=point)
    feature_collection = FeatureCollection([feature])
    #return jsonify(feature_collection)
    return jsonify(feature)

	
@app.route('/fire')
def fire():
    global i
    p0[0] += i
    p1[0] += i
    p2[0] += i
    p3[0] += i
    poly = Polygon([[p0, p1, p2, p3]])
    feature = Feature(geometry=poly)
    feature_collection = FeatureCollection([feature])
    #return jsonify(feature_collection)
    return jsonify(feature)

	
@app.route('/process')
def long_running_process():
      def generate():
        for row in range(1, 10):
            yield 'data: Processing \n\n'
            time.sleep(2)
      return Response(generate(), mimetype='text/event-stream')  

app.run(threaded=True, host='0.0.0.0')
