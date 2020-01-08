import requests
import geojson


''' telemetry
{
	'lat': 
	'lon':
	'alt':
	'vx':
	'vy':
	'vz':
}
polygons
Array of polygons
{
	'polygons':[...]
}

Single polygon
{
	'points': [...]
}

Single point
{
	'lat':
	'lon':
}

'''
delta = 0.0001

base_url = 'http://localhost:5000'
endpoints = {
	'telemetry_update': '/telemetry/update',
	'telemetry': '/telemetry',
	'polygons_update': '/polygon/update',
	'polygons': 'polygons'
}

def move_polygons():
    
    for polygon in polygons:
        for p in polygon['points']:
            p['lat'] = p['lat'] + delta

telemetry = {'lat': -8.318497, 'lon': 39.954263, 'alt': 1000,
             'vx': 50.0, 'vy': 50.0, 'vz': 0.0}

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


processed_polys = []
    for polygon in polygons:
            points = [geojson.Point((p['lat'], p['lon'])) for p in polygon['points']]
            poly = geojson.Polygon([points])
            processed_polys.append(geojson.Feature(geometry=poly))
    polygons_geojson = geojson.FeatureCollection(processed_polys)

data = jsonify(polygons_geojson).data
res = requests.post(url=base_url + endpoints['polygons_update'], data=data)