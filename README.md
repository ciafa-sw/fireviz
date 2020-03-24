README.md

# API
## UAV Telemetry
/telemetry
GET request that returns JSON formatted telemetry of UAV

```json
{
	'lat': 
	'lon':
	'alt':
	'vx':
	'vy':
	'vz':
}
```

/telemetry/update
POST request that receives JSON formatted UAV telemetry.

## Fire Telemetry
/polygons
GET request that returns GeoJSON formatted with polygons delineating fire fronts.

Example:
```json
{
  "features": [
    {
      "geometry": {
        "coordinates": [
          [
            [
              -8.305397, 
              39.954263
            ], 
            [
              -8.304897, 
              39.954263
            ], 
            [
              -8.304897, 
              39.959263
            ], 
            [
              -8.305397, 
              39.959263
            ]
          ]
        ], 
        "type": "Polygon"
      }, 
      "properties": {}, 
      "type": "Feature"
    }, 
    {
      "geometry": {
        "coordinates": [
          [
            [
              -8.304397, 
              39.955263
            ], 
            [
              -8.303897, 
              39.955263
            ], 
            [
              -8.303897, 
              39.960263
            ], 
            [
              -8.304397, 
              39.960263
            ]
          ]
        ], 
        "type": "Polygon"
      }, 
      "properties": {}, 
      "type": "Feature"
    }
  ], 
  "type": "FeatureCollection"
}
```

/polygons/update
POST request that receives GeoJSON formatted firefront polygons.