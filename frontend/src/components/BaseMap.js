import React, { Component } from "react";
import Distillery from "./Distillery";
import generateMap from "../utils/draw";

class BaseMap extends Component {
  constructor(props) {
    super(props);
    this.state = {
      distilleries: [{
        name: 'Something Park',
        region: 'Highland',
        yearEst: 1800
      }]
    }
  }
  componentDidMount() {
    fetch('/distilleries').then((data) => {
      console.log(data);
    });
    generateMap();
  }

  render() {
    return (
      <svg id="basemap">
        <g id="map"></g>
        {this.state.distilleries.map((d) => {
          <Distillery
            name={d.name}
            region="Highland"
            yearEst={d.year_established}
          />
        })}
      </svg>
    );
  }
}

export default BaseMap;
