import React, { Component } from "react";
import constants from '../utils/constants';

class Distillery extends Component {
  constructor(props) {
    super(props);
    this.state = {
      coordinates: [],
      active: false
    };
  }

  componentDidMount() {
    // Transform coordinates based on projection
    const { distillery } = this.props;
    const coordinates = constants.projection([distillery.latitude, distillery.longitude]);
    this.setState({coordinates});
  }

  render() {
    const { distillery } = this.props;

    return (
      <circle
        className="distillery"
        cx={this.state.coordinates[0]}
        cy={this.state.coordinates[1]}
        r={`${1 / Math.sqrt(this.props.zoomLevel)}px`}
        fill={this.state.active ? constants.colors[distillery.region] : "black"}
        data-name={distillery.name}
        data-region={distillery.region}
        data-year-est={distillery.year_established}
        onMouseOver={() => { this.setState({active: true}) }}
        onMouseLeave={() => { this.setState({active: false }) }}
      ></circle>
    );
  }
}

export default Distillery;
