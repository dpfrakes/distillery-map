import * as d3 from 'd3';
import React from 'react';
import * as topojson from "topojson-client";
import constants from './constants';

export default (distillery) => {

  console.log(distillery);

  // Define map size on screen
  // let width, height, svg, g, path, projection;

  let g = d3.select("svg g");

  // // Full width/height
  // width = window.innerWidth;
  // height = window.innerHeight;

  // svg = d3.select("body svg");

  // g = svg.append("g");

  // redraw(2);

  // svg.call(d3.zoom().on('zoom', function() {
  //   g.attr("transform", d3.event.transform);

  //   let dynamicScale = document.querySelector('g')
  //     .getAttribute('transform')
  //     .match(/.*(scale\(.*\)).*/)[1]
  //     .match(/\((.*)\)/)[1];

  //   // Add distillery locations to map
  //   // svg.selectAll("circle")
  //   //   .remove();

  //   redraw(2 / Math.sqrt(dynamicScale));
  // }));

  // path = d3.geoPath()
  //   .projection(projection);

  // d3.select(self.frameElement).style("height", height + "px");
  // g.attr("id", "map");

  // let redraw = (zoomScale) => {
  //   // Add distillery locations to map
  //   g.select(`circle[data-name="${distillery.name}"]`)
  //     .attr("class", "distillery")
  //     .attr("cx", (d) => projection(d.coordinates)[0])
  //     .attr("cy", (d) => projection(d.coordinates)[1])
  //     .attr("fill", (d) => constants.colors[d.region])
  //     .attr("data-name", (d) => d.name)
  //     .attr("data-region", (d) => d.region)
  //     .attr("data-year-est", (d) => d.year_established)
  //   }
}
