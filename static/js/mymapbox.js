
/* mapboxgl.accessToken = 'pk.eyJ1Ijoic291bGV5bWFuZWRpYWxsb28iLCJhIjoiY2p6c3FvMDc1MWpoODNjcGNvc29obW5pcSJ9.luUbRJXc8xnL38nNLkebeQ';
        var map = new mapboxgl.Map({
            container: 'map', // container id
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [-74.50, 40], // starting position
            zoom: 9 // starting zoom
        });

        // Add zoom and rotation controls to the map.
        map.addControl(new mapboxgl.NavigationControl()); */

/* mapboxgl.accessToken = 'pk.eyJ1Ijoic291bGV5bWFuZWRpYWxsb28iLCJhIjoiY2p6c3FvMDc1MWpoODNjcGNvc29obW5pcSJ9.luUbRJXc8xnL38nNLkebeQ';
var map = new mapboxgl.Map({
container: 'map', // container id
style: 'mapbox://styles/mapbox/streets-v11',
center: [-74.50, 40], // starting position
zoom: 9 // starting zoom
});

// Add zoom and rotation controls to the map.
map.addControl(new mapboxgl.NavigationControl());  */

// MDB Lightbox Init

mapboxgl.accessToken = 'pk.eyJ1Ijoic291bGV5bWFuZWRpYWxsb28iLCJhIjoiY2p6c3FvMDc1MWpoODNjcGNvc29obW5pcSJ9.luUbRJXc8xnL38nNLkebeQ';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/streets-v9',
center: [-122.486052, 37.830348],
zoom: 9
});

var geocoder = new MapboxGeocoder({
accessToken: mapboxgl.accessToken,
language: 'de-DE',
mapboxgl: mapboxgl
});
map.addControl(geocoder);
