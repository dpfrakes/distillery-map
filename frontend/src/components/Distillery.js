import React, { Component } from "react";
import * as d3 from 'd3';
import constants from '../utils/constants';
import drawDistillery from "../utils/drawDistillery";

class Distillery extends Component {
  constructor(props) {
    super(props);
    this.state = {
      coordinates: []
    };
  }

  componentDidMount() {
    // Transform coordinates based on projection
    const { distillery } = this.props;
    const projected = constants.projection([distillery.longitude, distillery.latitude]);
    this.setState({coordinates: projected});
  }

  render() {
    const distillery = this.props.distillery;

    return (
      <circle
        className="distillery"
        cx={this.state.coordinates[0]}
        cy={this.state.coordinates[1]}
        r="2px"
        fill={constants.colors[distillery.region]}
        data-name={distillery.name}
        data-region={distillery.region}
        data-year-est={distillery.year_established}
        data-original-coordinates={this.props.origCoord}
      ></circle>
    );
  }
}

export default Distillery;
