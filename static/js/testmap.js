var width = 960,
    height = 500,
    centered;

var projection = d3.geo.albersUsa()
    .scale(1070)
    .translate([width / 2, height / 2]);

var path = d3.geo.path()
    .projection(projection);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

svg.append("rect")
    .attr("class", "background")
    .attr("width", width)
    .attr("height", height)
    .on("click", clicked);

var g = svg.append("g");

d3.json("/mbostock/raw/4090846/us.json", function(error, us) {
  if (error) throw error;

  g.append("g")
      .attr("id", "states")
    .selectAll("path")
      .data(topojson.feature(us, us.objects.states).features)
    .enter().append("path")
      .attr("d", path)
      .on("click", clicked);

  g.append("path")
      .datum(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; }))
      .attr("id", "state-borders")
      .attr("d", path);
});

function clicked(d) {
  var x, y, k;

  if (d && centered !== d) {
    var centroid = path.centroid(d);
    x = centroid[0];
    y = centroid[1];
    k = 4;
    centered = d;
  } else {
    x = width / 2;
    y = height / 2;
    k = 1;
    centered = null;
  }

  g.selectAll("path")
      .classed("active", centered && function(d) { return d === centered; });

  g.transition()
      .duration(750)
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
      .style("stroke-width", 1.5 / k + "px");
}

// deltas = [-100, -4, -1, 0]

// map = {
//   const svg = d3.create("svg")
//       .attr("viewBox", [0, 0, width, height]);

//   const tile = d3.tile()
//       .extent([[0, 0], [width, height]])
//       .tileSize(512)
//       .clampX(false);

//   const zoom = d3.zoom()
//       .scaleExtent([1 << 8, 1 << 22])
//       .extent([[0, 0], [width, height]])
//       .on("zoom", () => zoomed(d3.event.transform));

//   const levels = svg.append("g")
//       .attr("pointer-events", "none")
//     .selectAll("g")
//     .data(deltas)
//     .join("g")
//       .style("opacity", showlayers ? 0.3 : null);

//   svg
//       .call(zoom)
//       .call(zoom.transform, transform);

//   function zoomed(transform) {
//     transform = transform;

//     levels.each(function(delta) {
//       const tiles = tile.zoomDelta(delta)(transform);

//       d3.select(this)
//         .selectAll("image")
//         .data(tiles, d => d)
//         .join("image")
//           .attr("xlink:href", d => url(...d3.tileWrap(d)))
//           .attr("x", ([x]) => (x + tiles.translate[0]) * tiles.scale)
//           .attr("y", ([, y]) => (y + tiles.translate[1]) * tiles.scale)
//           .attr("width", tiles.scale)
//           .attr("height", tiles.scale);
//     });
//   }

//   return svg.node();
// }

// transform = d3.zoomIdentity.translate(width >> 1, height >> 1).scale(1 << 12)

// url = (x, y, z) => `https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/${z}/${x}/${y}${devicePixelRatio > 1 ? "@2x" : ""}?access_token=pk.eyJ1IjoidG1jdyIsImEiOiJjamN0Z3ZiOXEwanZkMnh2dGFuemkzemE3In0.gibebYiJ5TEdXvwjpCY0jg`

// height = 600

// d3 = require("d3@5", "d3-tile@1")
