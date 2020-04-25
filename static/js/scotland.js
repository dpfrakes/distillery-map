var colors = {
  Speyside: 'red',
  Lowland: 'orange',
  Highland: 'green',
  Islay: 'blue',
  Island: 'brown',
  Campbeltown: 'purple',
  Other: 'white',
}

var generateMap = function() {

  // Define map size on screen
  var width, height, svg, g, path, projection;

  // Full width/height
  width = window.innerWidth;
  height = window.innerHeight;

  console.log(`W: ${width} | H: ${height}`);

  // Mercator projection
  projection = d3.geoMercator()
    // Centroid approximated by centering Scotland in Google Maps, copying coordinates, then adjusting/rounding
    .center([-9, 58])
    // Scale based on trial and error to fill screen with Scottish mainland
    .scale(4500)
    // Center
    .translate([width / 2, height / 2]);

  svg = d3.select("body svg")
    .attr("width", width)
    .attr("height", height);

  g = svg.append("g");

  d3.json(mapFile).then(ready);

  path = d3.geoPath()
    .projection(projection);

  d3.select(self.frameElement).style("height", height + "px");
  g.attr("id", "map");

  // DEBUG mouse move on svg
  // var debugOutput = document.getElementById('mouse-coordinates');
  // document.querySelector('svg').onmousemove = function clicked(evt) {
  //   var e = evt.target;
  //   var dim = e.getBoundingClientRect();
  //   var x = evt.clientX - dim.left;
  //   var y = evt.clientY - dim.top;
  //   debugOutput.innerHTML = "x: " + x + " y:" + y;
  // }

  document.querySelectorAll('circle').forEach(function(c) {
    console.log(c);
    // c.onmousemove = function() { console.log(c); }
  });

  function redraw(distilleries, zoomScale) {
    // Add distillery locations to map
    g.selectAll("circle")
      .data(distilleries)
      .enter()
      .append("circle")
      .attr("class", "distillery")
      .attr("cx", (d) => projection(d.coordinates)[0])
      .attr("cy", (d) => projection(d.coordinates)[1])
      .attr("r", zoomScale + "px")
      .attr("fill", (d) => colors[d.region])
      .attr("data-name", (d) => d.name)
      .attr("data-region", (d) => d.region)
      .attr("data-year-est", (d) => d.year_established)
  }

  function ready(shp, err) {

    // Extracting polygons and contours
    var scotland = topojson.feature(shp, shp.objects.eer);

    // Draw Scotland map
    g.selectAll(".country")
      .data(scotland.features)
      .enter()
      .append("path")
      .attr("class", "country")
      .attr("d", path);

    redraw(distilleries, 2);

    svg.call(d3.zoom().on('zoom', function() {
      g.attr("transform", d3.event.transform);

      dynamicScale = document.querySelector('g')
        .getAttribute('transform')
        .match(/.*(scale\(.*\)).*/)[1]
        .match(/\((.*)\)/)[1];

      // Add distillery locations to map
      svg.selectAll("circle")
        .remove();

      redraw(distilleries, 2 / Math.sqrt(dynamicScale));
    }));
  }
}

document.addEventListener('DOMContentLoaded', generateMap);
// window.onresize = generateMap;
