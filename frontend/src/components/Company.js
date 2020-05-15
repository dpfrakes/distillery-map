import React, { Component } from "react";
import constants from '../utils/constants';

class Company extends Component {
  constructor(props) {
    super(props);
    this.state = {
      coordinates: []
    };
  }

  componentDidMount() {
    // Transform coordinates based on projection
    const { company } = this.props;
    const projected = constants.projection([company.latitude, company.longitude]);
    this.setState({coordinates: projected});
  }

  render() {
    const company = this.props.company;

    return (
      <rect
        className="company"
        x={this.state.coordinates[0]}
        y={this.state.coordinates[1]}
        width="5px"
        height="5px"
        data-name={company.name}
      />
    );
  }
}

export default Company;
