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

  svg.call(d3.zoom().on('zoom', function() {

    console.warn('nope stop everything');
    d3.event.preventDefault();

    g.attr("transform", d3.event.transform);

    // Add distillery locations to map
    svg.selectAll("circle")
      .remove();

    // redraw(distilleries, 2 / Math.sqrt(dynamicScale));

    // Add distillery locations to map
    g.selectAll("circle")
      .data(distilleries)
      .enter()
      .append("circle")
      .attr("class", "distillery")
      .attr("cx", (d) => projection(d.coordinates)[0])
      .attr("cy", (d) => projection(d.coordinates)[1])
      .attr("r", "2px")
      .attr("fill", (d) => constants.colors[d.region])
      .attr("data-name", (d) => d.name)
      .attr("data-region", (d) => d.region)
      .attr("data-year-est", (d) => d.year_established)
      // .on("mouseover", function(d) {		
      //   div.transition()		
      //       .duration(200)		
      //       .style("opacity", .9);		
      //   div	.html(formatTime(d.date) + "<br/>"  + d.close)	
      //       .style("left", (d3.event.pageX) + "px")		
      //       .style("top", (d3.event.pageY - 28) + "px");	
      //   })					
      // .on("mouseout", function(d) {		
      //     div.transition()		
      //         .duration(500)		
      //         .style("opacity", 0);	
      // });
  
  }));

  path = d3.geoPath()
    .projection(constants.projection);

  g.attr("id", "map");

}
