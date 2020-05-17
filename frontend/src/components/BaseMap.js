import React, { Component } from "react";
import * as topojson from "topojson-client";
import * as d3 from "d3";

import Company from "./Company";
import Search from "./Search";
import Tooltip from "./Tooltip";
import constants from "../utils/constants";

class BaseMap extends Component {
  constructor(props) {
    super(props);
    this.state = {
      // Light/dark mode
      darkMode: true,

      // Track status
      mapLoaded: false,
      companiesLoaded: false,
      distilleriesLoaded: false,

      // Data collected from BE
      companies: [],
      distilleries: [],
      connections: [],

      // Active entity {"type": "...", "info": {...}}
      activeEntity: {},

      // Propagate d3 zoom level to redraw child components
      zoomLevel: 1
    };

    this.path = d3.geoPath()
      .projection(constants.projection);

    this._onHover = this._onHover.bind(this);
    this._toggleDarkMode = this._toggleDarkMode.bind(this);
    this._connectEntities = this._connectEntities.bind(this);
    this._activate = this._activate.bind(this);
  }

  componentDidMount() {

    // Render base map
    let svg = d3.select("body svg")
      .attr("width", window.innerWidth)
      .attr("height", window.innerHeight);
    let g = d3.select("svg g");

    // Draw world
    d3.json("/static/json/topo-uk.json").then((shp, err) => {

      // Extract polygons and contours
      var k = Object.keys(shp.objects)[0];
      var world = topojson.feature(shp, shp.objects[k]);

      // Draw map
      g.selectAll(".country")
        .data(world.features)
        .enter()
        .append("path")
        .attr("class", "country")
        .attr("d", this.path);

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
      this.setState({zoomLevel: d3.event.transform.k});
    }));
  }

  _toggleDarkMode(e) {
    this.setState({darkMode: !this.state.darkMode});
  }

  _connectEntities() {
    // Draw connections between companies and distilleries
    if (this.state.distilleriesLoaded && this.state.companiesLoaded) {
      let connections = [];
      this.state.companies.forEach((c) => {
        c.distilleries.forEach((d) => {
          if (d.latitude && d.longitude && c.latitude && c.longitude)
            connections.push({type: "LineString", coordinates: [[d.latitude, d.longitude], [c.latitude, c.longitude]]});
        })
      });
      this.setState({connections});
    }
  }

  _onHover(e) {
    // Hover listener on parent element since:
    // 1. Tooltip is controlled by BaseMap
    // 2. Cannot implement onMouseOver directly on React component
    // 3. Distillery component renders as <circle> immediately inside <svg> (no good DOM structure alternatives)
    let activeEntity;

    if (this.state.persistActive) return;

    if (e.target.classList[0] == 'distillery') {
      let { distilleries } = this.state || [];
      activeEntity = {
        type: "distillery",
        info: distilleries.filter((d) => d.name == e.target.getAttribute('data-name'))[0]
      }
    } else if (e.target.classList[0] == 'company') {
      let { companies } = this.state || [];
      activeEntity = {
        type: "company",
        info: companies.filter((d) => d.name == e.target.getAttribute('data-name'))[0]
      }
    }
    this.setState({activeEntity});
  }

  _activate(entitySection, entityName) {
    if (entitySection == 'distilleries') {
      this.setState({
        activeEntity: {
          type: "distillery",
          info: this.state.distilleries.filter((d) => d.name == entityName)[0]
        },
        persistActive: true
      });
    } else if (entitySection == 'companies') {
      this.setState({
        activeEntity: {
          type: "company",
          info: this.state.companies.filter((c) => c.name == entityName)[0]
        },
        persistActive: true
      });
    } else {
      console.error(`Unsupported entity type selected from search dropdown: ${entityName}`);
    }
  }

  render() {
    // Place all drawn shapes inside <g> to share transform
    return (
      <>
        <div id="map" className={this.state.darkMode ? "dark" : ""}>
          <div style={{position: "absolute", bottom: 20, right: 20, background: "rgba(255, 255, 255, 0.5)", width: 300, padding: 10, fontFamily: "monospace"}}>
              <p>{this.state.companiesLoaded ? "✅ " : "..."}companies</p>
              <p>{this.state.distilleriesLoaded ? "✅ " : "..."}distilleries</p>
              <p>{this.state.mapLoaded ? "✅ " : "..."}map</p>
          </div>
          <button id="toggle-ui-mode" onClick={this._toggleDarkMode}>{this.state.darkMode ? "light" : "dark"}</button>
          <svg onMouseOver={this._onHover}>
            <g>
              {this.state.companiesLoaded && this.state.companies.filter((c) => !!c.latitude && c.longitude).map((c, i) =>
                <Company key={i} company={c} path={this.path} zoomLevel={this.state.zoomLevel} active={this.state.activeEntity ? this.state.activeEntity.info == c : false} />
              )}
            </g>
          </svg>
        </div>
        <Search distilleries={this.state.distilleries} companies={this.state.companies} onSelect={this._activate} />
        <Tooltip entity={this.state.activeEntity} />
      </>
    );
  }
}

export default BaseMap;
