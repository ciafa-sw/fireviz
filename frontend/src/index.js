// start elm app

// setup ports

// start map

mapboxgl.accessToken = '{{MAPBOX_ACCESS_KEY}}';

var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/satellite-v9',
    center: [-8.318497, 39.954263],
    zoom: 12,
});

// port functions

addUavSource(data){
    console.debug("JS | adding UAV source")
    map.addSource('drone', { type: 'geojson', data: drone_url });
    map.addLayer({
        "id": "drone",
        "type": "symbol",
        "source": "drone",
        "layout": {
        "icon-image": "rocket-15"
        }
    }); // add layer drone

}

addFireSource(){
    console.debug("JS | adding fire source (Polygon)")
    map.addSource('fire', { type: 'geojson', data: fire_url });
    map.addLayer({
        'id': 'fire',
        'type': 'fill',
        'source': "fire",
        'layout': {},
        'paint': {
            'fill-color': '#ed6300',
            'fill-opacity': 0.8
        },
        'filter': ['==', '$type', 'Polygon']
    }); // add layer fire 
}

updateSource(data){
    console.debug("JS | updating source")
    map.getSource(data.sourceName).setData(drone_url);

}

// when map is loaded, signal elm app

map.on('load', function () {
    console.debug("JS | Map loaded.")
    elmApp.port.send(signal)
}); //map on load


