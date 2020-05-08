import React, { Component } from "react";
import Distillery from "./Distillery";
import Tooltip from "./Tooltip";
import drawScotland from "../utils/draw";
import constants from "../utils/constants";
import * as d3 from "d3";

class BaseMap extends Component {
  constructor(props) {
    super(props);
    this.state = {
      darkMode: true,
      loaded: true,
      distilleries: [],
      activeDistillery: {}
    };
    this._onHover = this._onHover.bind(this);
    this._toggleDarkMode = this._toggleDarkMode.bind(this);
  }

  componentDidMount() {

    // render map of country only
    drawScotland();

    // fetch distillery data from API
    fetch('/api/distilleries/')
      .then((data) => data.json())
      .then((res) => {
        this.setState({distilleries: res.results, loaded: true});
      });

    // Let React handle click/drag/zoom
    let svg = d3.select("svg");
    let g = d3.select("svg g");

    svg.call(d3.zoom().on('zoom', () => {
      g.attr("transform", d3.event.transform);

      // Add distillery locations to map
      svg.selectAll("circle")
        .remove();

      // Add distillery locations to map
      g.selectAll("circle")
        .data(this.state.distilleries.filter((d) => !!d.latitude && !!d.longitude))
        .enter()
        .append("circle")
        .attr("class", "distillery")
        .attr("cx", (d) => constants.projection([d.latitude, d.longitude])[0])
        .attr("cy", (d) => constants.projection([d.latitude, d.longitude])[1])
        .attr("r", (d) => 2 / Math.sqrt(d3.event.transform.k) + "px")
        .attr("fill", (d) => constants.colors[d.region])
        .attr("data-name", (d) => d.name)
        .attr("data-region", (d) => d.region)
        .attr("data-year-est", (d) => d.year_established)
      // let distilleries = this.state.distilleries.map((d) => {
      //   if (!!d.latitude && !!d.longitude) {
      //     let projected = constants.projection([d.latitude, d.longitude]);
      //     console.log(projected);
      //     d.cx = projected[0];
      //     d.cy = projected[1];
      //   }
      //   return d;
      // });
      // this.setState({ distilleries });
    }));
  }

  _toggleDarkMode(e) {
    this.setState({darkMode: !this.state.darkMode});
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
    return this.state.loaded && (
      <div id="map" className={this.state.darkMode ? "dark" : ""}>
        <button id="toggle-ui-mode" onClick={this._toggleDarkMode}>{this.state.darkMode ? "light" : "dark"}</button>
        <svg onMouseOver={this._onHover}>
          {this.state.distilleries.filter((d) => !!d.latitude && d.longitude).map((d, i) =>
            <Distillery key={i} distillery={d} />
          )}
        </svg>
        <Tooltip distillery={this.state.activeDistillery} />
      </div>
    );
  }
}

export default BaseMap;
