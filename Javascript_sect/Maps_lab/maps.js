// js maps



const url= 'https://jsonplaceholder.typicode.com/users'

axios.get(url)

.then(function (response) { 


  data = response.data 
  
  for (let i = 0; i < data.length; i++) {
    let marker = L.marker([data[i].address.geo.lat, data[i].address.geo.lng]).addTo(mymap);
  }})
  // console.log(data[0].address.geo)



let mymap = L.map('mapid').setView([51.505, -0.09], 2);


L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: 'pk.eyJ1IjoiZWxtaWNoZSIsImEiOiJjazQwb2s2NHowM3Y4M2xwbjJ2NXJhZXZ1In0.-bKylG4SBc4ybZCodZGzKQ'
}).addTo(mymap); 