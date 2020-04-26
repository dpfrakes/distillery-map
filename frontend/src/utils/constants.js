import * as d3 from "d3";

export default {
  projection: d3.geoMercator()
    // Centroid approximated by centering Scotland in Google Maps, copying coordinates, then adjusting/rounding
    .center([-4, 57])
    // Scale based on trial and error to fill screen with Scottish mainland
    .scale(4500)
    // Center
    .translate([window.innerWidth / 2, window.innerHeight / 2]),
  colors: {
    Speyside: 'red',
    Lowland: 'orange',
    Highland: 'green',
    Islay: 'blue',
    Island: 'brown',
    Campbeltown: 'purple',
    Other: 'white',
  }
}
