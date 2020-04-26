import React, { Component } from "react";
import Distillery from "./Distillery";
import Tooltip from "./Tooltip";
import drawScotland from "../utils/drawCountry";
import * as d3 from "d3";

class BaseMap extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loaded: true,
      distilleries: [],
      activeDistillery: {}
    };
    this.onHover = this.onHover.bind(this);
  }

  componentDidMount() {

    // render map of country only
    drawScotland();

    // fetch distillery data from API
    fetch('/api/distilleries/')
      .then((data) => data.json())
      .then((distilleries) => {
        this.setState({distilleries, loaded: true});
      });

    // Let React handle click/drag/zoom
    let svg = d3.select("svg");
    let g = d3.select("svg g");
    // const forceUpdate = this.forceUpdate;

    // svg.call(d3.zoom().on('zoom', () => {
    //   g.attr("transform", d3.event.transform);
    //   // d3.event.preventDefault();
    //   // redraw by forcing update
    //   // this.setState({distilleries: state.distilleries});
    //   forceUpdate();
    // }));

  }

  onHover(e) {
    // Hover listener on parent element since:
    // 1. Tooltip controlled by BaseMap
    // 2. Cannot implement onMouseOver directly on React component
    // 3. Distillery component renders as <circle> immediately inside <svg> (no good DOM structure alternatives)
    if (e.target.classList[0] == 'distillery') {
      let { distilleries } = this.state;
      let activeDistillery = distilleries.filter((d) => d.name == e.target.getAttribute('data-name'))[0];
      this.setState({activeDistillery});
    } else {
      this.setState({activeDistillery: undefined});
    }
  }

  render() {
    return this.state.loaded && (
      <>
        <svg onMouseOver={this.onHover}>
          {this.state.distilleries.map((d, i) =>
            <Distillery key={i} distillery={d} origCoord={d.coordinates} />
          )}
        </svg>
        <Tooltip distillery={this.state.activeDistillery} />
      </>
    );
  }
}

export default BaseMap;
