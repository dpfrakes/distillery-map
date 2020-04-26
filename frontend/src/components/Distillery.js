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
    this.setState({coordinates: constants.projection([distillery.latitude, distillery.longitude])})
  }

  render() {
    const distillery = this.props.distillery;

    return (
      <circle
        className="distillery"
        cx="300"
        cy="300"
        r="2px"
        fill={constants.colors[distillery.region]}
        data-name={distillery.name}
        data-region={distillery.region}
        data-year-est={distillery.year_established}
      ></circle>
    );
  }
}

export default Distillery;
