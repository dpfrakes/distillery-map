import React, { Component } from "react";
import generateMap from "../utils/draw";

class BaseMap extends Component {
  componentDidMount() {
    generateMap();
  }

  render() {
    return (
      <svg id="basemap"></svg>
    );
  }
}

export default BaseMap;
