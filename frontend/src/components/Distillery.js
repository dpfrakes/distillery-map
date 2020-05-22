import React, { Component } from "react";
import constants from '../utils/constants';

class Distillery extends Component {
  constructor(props) {
    super(props);
    this.state = {
      coordinates: [],
      active: false
    };
    this._handleMouse = this._handleMouse.bind(this);
  }

  _handleMouse(e) {
    // Set to active if event is mouseover (otherwise deactivate)
    const active = e.type == 'mouseover';
    this.setState({active});

    // Use callback function to notify parent element to highlight connection accordingly
    this.props.cb(active ? this.props.distillery : '');
  }

  componentDidMount() {
    // Transform coordinates based on projection
    const { distillery } = this.props;
    const coordinates = constants.projection([distillery.latitude, distillery.longitude]);
    this.setState({coordinates});
  }

  render() {
    const { distillery } = this.props;

    return this.state.coordinates && (
      <circle
        className="distillery"
        cx={this.state.coordinates[0]}
        cy={this.state.coordinates[1]}
        r={`${1 / Math.sqrt(this.props.zoomLevel)}px`}
        fill={this.state.active ? constants.colors[distillery.region] : "black"}
        data-name={distillery.name}
        data-region={distillery.region}
        data-year-est={distillery.year_established}
        onMouseOver={this._handleMouse}
        onMouseLeave={this._handleMouse}
      ></circle>
    );
  }
}

export default Distillery;
