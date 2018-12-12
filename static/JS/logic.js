// Create the tile layer that will be the background of our map
var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});

var layers = {
    governer: new L.LayerGroup(),
    senate: new L.LayerGroup(),
};

var map = L.map("map-id", {
    center: [40.4173, -82.9071],
    zoom: 7,
    layers: [
        layers.governer,
        layers.senate,
    ]
});
  
lightmap.addTo(map);

var overlays = {
    "Governer": layers.governer,
    "Senate": layers.senate,
};

L.control.layers(null, overlays).addTo(map);

var info = L.control({
    position: "bottomright"
});
// When the layer control is added, insert a div with the class of "legend"
info.onAdd = function() {
    var div = L.DomUtil.create("div", "legend");
    return div;
};
  // Add the info legend to the map
info.addTo(map);

var link = "../../usa-2016-presidential-election-by-county (6).geojson";
console.log(link)


function fillcoloring (votes){
  if (votes >= 47.8){
    fillColor = "blue";
  }
  else{
    fillColor="red";
  }
}; 

function chooseColor(winner){
  switch (winner){
  case "39095":
    return "blue";
  case "39061":
    return "blue";
  case "39049":
    return "blue";  
  case "39009":
    return "blue";
  case "39035":
    return "blue";   
  case "39153":
    return "blue";
  default:
    return "red";
  }
};

  // Grabbing our GeoJSON data..
d3.json(link, function(data) {
    d3.csv("governers2.csv", function (response){
      console.log(data);
      var data2 = [response]
      console.log(data2);
      
  
      L.geoJson(data, {
        // Style each feature (in this case a neighborhood)
        style: function(feature) {
          return {
            color: "white",
            

            fillColor: chooseColor(feature.properties.fips),
            fillOpacity: 0.5,
            weight: 1.5
          };
        },
        // Called on each feature
        onEachFeature: function(feature, layer) {
          // Set mouse events to change map styling
          layer.on({
            // When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 90% so that it stands out
            mouseover: function(event) {
              layer = event.target;
              layer.setStyle({
                fillOpacity: 0.9
              });
            },
            // When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 50%
            mouseout: function(event) {
              layer = event.target;
              layer.setStyle({
                fillOpacity: 0.5
              });
            },
            
          });
          // Giving each feature a pop-up with information pertinent to it
          layer.bindPopup("<h1>" + feature.properties.county + "</h1> <hr>" + "<h2> Dem %: " + feature.properties.dem16_frac + "</h2><h2> Rep %: " + feature.properties.rep16_frac + "</h2>" +
          '<a href="{{{feature.properties.fips_count}}}">Visit County</a>');
    
        }
      }).addTo(map);
    });
  });


   