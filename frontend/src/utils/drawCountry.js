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

  d3.json("/static/json/topo-scotland.json").then((shp, err) => {

    // Extracting polygons and contours
    var scotland = topojson.feature(shp, shp.objects.eer);
  
    // Draw Scotland map
    g.selectAll(".country")
      .data(scotland.features)
      .enter()
      .append("path")
      .attr("class", "country")
      .attr("d", path);
  });

  path = d3.geoPath()
    .projection(constants.projection);

}
