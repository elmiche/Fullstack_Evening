

var mymap = L.map('mapid').setView([45.50, -122.67], 13);


L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: 'pk.eyJ1IjoiZWxtaWNoZSIsImEiOiJjazQwb2s2NHowM3Y4M2xwbjJ2NXJhZXZ1In0.-bKylG4SBc4ybZCodZGzKQ'
}).addTo(mymap);