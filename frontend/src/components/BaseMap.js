import React, { Component } from "react";
import * as topojson from "topojson-client";
import * as d3 from "d3";

import Company from "./Company";
import Distillery from "./Distillery";
import Tooltip from "./Tooltip";
import constants from "../utils/constants";

class BaseMap extends Component {
  constructor(props) {
    super(props);
    this.state = {
      darkMode: true,
      mapLoaded: false,
      companiesLoaded: false,
      distilleriesLoaded: false,
      companies: [],
      distilleries: [],
      connections: [],
      activeDistillery: {}
    };
    this._onHover = this._onHover.bind(this);
    this._toggleDarkMode = this._toggleDarkMode.bind(this);
    this._connectEntities = this._connectEntities.bind(this);
  }

  componentDidMount() {

    // Render base map
    let svg, g, path;
    svg = d3.select("body svg")
      .attr("width", window.innerWidth)
      .attr("height", window.innerHeight);

    g = d3.select("svg g");

    path = d3.geoPath()
      .projection(constants.projection);

    // Draw world
    d3.json("/static/json/topo-world.json").then((shp, err) => {

      // Extract polygons and contours
      var k = Object.keys(shp.objects)[0];
      var world = topojson.feature(shp, shp.objects[k]);

      // Draw map
      g.selectAll(".country")
        .data(world.features)
        .enter()
        .append("path")
        .attr("class", "country")
        .attr("d", path);
      
      // Update state
      this.setState({mapLoaded: true});
    });

    // Fetch distillery data from API
    fetch('/api/distilleries/')
      .then((data) => data.json())
      .then((res) => {
        this.setState({distilleries: res.results, distilleriesLoaded: true}, this._connectEntities);
      });

    // Fetch company data from API
    fetch('/api/companies/')
      .then((data) => data.json())
      .then((res) => {
        this.setState({companies: res.results, companiesLoaded: true}, this._connectEntities);
      });

    // Let React handle click/drag/zoom
    svg.call(d3.zoom().on('zoom', () => {
      // Set transform based on zoom/translation
      g.attr("transform", d3.event.transform);

      // Re-draw distilleries
      g.selectAll("circle")
        .remove();
      g.selectAll("circle")
        .data(this.state.distilleries.filter((d) => !!d.latitude && !!d.longitude))
        .enter()
        .append("circle")
        .attr("class", "distillery")
        .attr("cx", (d) => constants.projection([d.latitude, d.longitude])[0])
        .attr("cy", (d) => constants.projection([d.latitude, d.longitude])[1])
        .attr("r", (d) => 1 / Math.sqrt(d3.event.transform.k) + "px")
        .attr("fill", (d) => constants.colors[d.region])
        .attr("data-name", (d) => d.name)
        .attr("data-region", (d) => d.region)
        .attr("data-year-est", (d) => d.year_established);

      // Re-draw all companies
      g.selectAll("rect")
        .remove();
      g.selectAll("rect")
        .data(this.state.companies.filter((c) => !!c.latitude && !!c.longitude))
        .enter()
        .append("rect")
        .attr("class", "company")
        .attr("x", (c) => constants.projection([c.latitude, c.longitude])[0])
        .attr("y", (c) => constants.projection([c.latitude, c.longitude])[1])
        .attr("width", (c) => 5 / Math.sqrt(d3.event.transform.k) + "px")
        .attr("height", (c) => 5 / Math.sqrt(d3.event.transform.k) + "px");

      // Re-draw all connections
      g.selectAll(".connection")
        .remove();
      g.selectAll(".connection")
        .data(this.state.connections)
        .enter()
        .append("path")
        .attr("d", (p) => path(p))
        .style("fill", "none")
        .style("stroke", "orange")
        .style("stroke-width", 3);

        // Draw world
    var links = [{type: "LineString", coordinates: [[100, 60], [30, 0]]}]

    }));
  }

  _toggleDarkMode(e) {
    this.setState({darkMode: !this.state.darkMode});
  }

  _connectEntities() {
    console.log(`[${this.state.distilleriesLoaded ? 'x' : ' '}] distilleries loaded`)
    console.log(`[${this.state.companiesLoaded ? 'x' : ' '}] companies loaded`)
    if (this.state.distilleriesLoaded && this.state.companiesLoaded) {
      console.log('make those connections@!');
    }
  }

  _onHover(e) {
    // Hover listener on parent element since:
    // 1. Tooltip is controlled by BaseMap
    // 2. Cannot implement onMouseOver directly on React component
    // 3. Distillery component renders as <circle> immediately inside <svg> (no good DOM structure alternatives)
    if (e.target.classList[0] == 'distillery') {
      let { distilleries } = this.state || [];
      let activeDistillery = distilleries.filter((d) => d.name == e.target.getAttribute('data-name'))[0];
      this.setState({activeDistillery});
    } else {
      this.setState({activeDistillery: undefined});
    }
  }

  render() {
    // Place all drawn shapes inside <g> to share transform
    return (
      <div id="map" className={this.state.darkMode ? "dark" : ""}>
        <div style={{position: "absolute", bottom: 20, right: 20, background: "rgba(255, 255, 255, 0.5)", width: 300, padding: 10, fontFamily: "monospace"}}>
            <p>{this.state.companiesLoaded ? "✅ " : "..."}companies</p>
            <p>{this.state.distilleriesLoaded ? "✅ " : "..."}distilleries</p>
            <p>{this.state.mapLoaded ? "✅ " : "..."}map</p>
        </div>
        <button id="toggle-ui-mode" onClick={this._toggleDarkMode}>{this.state.darkMode ? "light" : "dark"}</button>
        <svg onMouseOver={this._onHover}>
          <g>
            {this.state.distilleriesLoaded && this.state.distilleries.filter((d) => !!d.latitude && d.longitude).map((d, i) =>
              <Distillery key={i} distillery={d} />
            )}
            {this.state.companiesLoaded && this.state.companies.filter((c) => !!c.latitude && c.longitude).map((c, i) =>
              <Company key={i} company={c} />
            )}
          </g>
        </svg>
        <Tooltip distillery={this.state.activeDistillery} />
      </div>
    );
  }
}

export default BaseMap;
