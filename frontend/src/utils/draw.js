import * as d3 from 'd3';
import * as topojson from "topojson-client";
import constants from "./constants";

export default () => {

  // Define map size on screen
  let svg, g, path;

  svg = d3.select("body svg")
    .attr("width", window.innerWidth)
    .attr("height", window.innerHeight);

  g = svg.append("g");

  // Draw world
  d3.json("/static/json/topo-world.json").then((shp, err) => {

    // Extracting polygons and contours
    var k = Object.keys(shp.objects)[0];
    var world = topojson.feature(shp, shp.objects[k]);
  
    // Draw Scotland map
    g.selectAll(".country")
      .data(world.features)
      .enter()
      .append("path")
      .attr("class", "country")
      .attr("d", path);
  });

  // Draw Scotland
  // d3.json("/static/json/topo-scotland.json").then((shp, err) => {

  //   // Extracting polygons and contours
  //   var scotland = topojson.feature(shp, shp.objects.eer);
  
  //   // Draw Scotland map
  //   g.selectAll(".country")
  //     .data(scotland.features)
  //     .enter()
  //     .append("path")
  //     .attr("class", "country")
  //     .attr("d", path);
  // });

  path = d3.geoPath()
    .projection(constants.projection);

}
