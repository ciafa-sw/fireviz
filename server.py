
import os, time
from flask import Flask, Response, render_template, jsonify, request
import geojson

app = Flask(__name__)
app.debug = True

#ACCESS_KEY = os.environ.get('MAPBOX_ACCESSKEY')
MAPBOX_ACCESS_KEY = 'pk.eyJ1IjoiZGlvZ29hb3MiLCJhIjoiY2p6YmMydDM4MDA0YTNqbzB4Y2JuOWV6MyJ9.57byXweMGWHJztAUs_P2Cw'

global i
i = 0.0001



m0 = {'lat': -8.318497, 'lon': 39.954263}
m1 = {'lat': -8.318497+0.0005, 'lon': 39.954263}
m2 = {'lat': -8.318497+0.0005, 'lon': 39.954263+0.005}
m3 = {'lat': -8.318497, 'lon': 39.954263+0.005}

m4 = {'lat': -8.318497+0.001, 'lon': 39.954263+0.001}
m5 = {'lat': -8.318497+0.0005+0.001, 'lon': 39.954263+0.001}
m6 = {'lat': -8.318497+0.0005+0.001, 'lon': 39.954263+0.005+0.001}
m7 = {'lat': -8.318497+0.001, 'lon': 39.954263+0.005+0.001}
poly0 = {'points': [m0, m1, m2, m3]}
poly1 = {'points': [m4, m5, m6, m7]}

polygons = [poly0, poly1]

telemetry = {'lat': None, 'lon': None, 'alt': None,
             'vx': None, 'vy': None, 'vz': None}
polygons_geojson = geojson.FeatureCollection([])


@app.route('/')
def index():
    # UPDATE_FREQUENCY determines period of 
    return render_template('index2.html', MAPBOX_ACCESS_KEY=MAPBOX_ACCESS_KEY, UPDATE_PERIOD=1000)


@app.route('/result')
def get_drone_position():
    global i
    point = geojson.Point((-8.318497+i, 39.954263))
    i += 0.0001
    feature = geojson.Feature(geometry=point)
    feature_collection = geojson.FeatureCollection([feature])
    #return jsonify(feature_collection)
    return jsonify(feature)

	
@app.route('/fire')
def fire():
    global i
    p0[0] += i
    p1[0] += i
    p2[0] += i
    p3[0] += i
    poly = geojson.Polygon([[p0, p1, p2, p3]])
    feature = geojson.Feature(geometry=poly)
    polygons_geojson = geojson.FeatureCollection([feature])
    #return jsonify(polygons_geojson)
    return jsonify(feature)


def move_polygons():
    delta = 0.0001
    for polygon in polygons:
        for p in polygon['points']:
            p['lat'] = p['lat'] + delta

@app.route('/fire2')
def fire2():
    move_polygons()
    processed_polys = []
    for polygon in polygons:
            points = [geojson.Point((p['lat'], p['lon'])) for p in polygon['points']]
            poly = geojson.Polygon([points])
            processed_polys.append(geojson.Feature(geometry=poly))
    polygons_geojson = geojson.FeatureCollection(processed_polys)
    #print(jsonify(polygons_geojson).data)
    return jsonify(polygons_geojson)
	
@app.route('/process')
def long_running_process():
      def generate():
        for row in range(1, 10):
            yield 'data: Processing \n\n'
            time.sleep(2)
      return Response(generate(), mimetype='text/event-stream')  


# returns current telemetry of UAV, GET request
@app.route('/telemetry', methods = ['GET'])
def get_telemetry():
    raise NotImplementedError()

# updates telemetry of UAV, POST request
@app.route('/telemetry/update', methods = ['POST'])
def update_telemetry(data):
    raise NotImplementedError()

# updates firefronts, POST REQUEST
@app.route('/polygons/update', methods = ['POST'])
def update_polygons(data):
    #raise NotImplementedError()
    print('polygon update')
    content = request.get_json()
    print(content)
    

app.run(threaded=True, host='0.0.0.0')
