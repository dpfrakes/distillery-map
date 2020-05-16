import React, { Component } from "react";
import Distillery from "./Distillery";
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
    const { company } = this.props;

    return (
      <>
        <rect
          className="company"
          x={this.state.coordinates[0]}
          y={this.state.coordinates[1]}
          width="5px"
          height="5px"
          data-name={company.name}
        />
        {company.distilleries.map((d, i) => {
          return (
            <React.Fragment key={i}>
              <path
                className="connection"
                d={this.props.path({type: "LineString", coordinates: [[d.latitude, d.longitude], [company.latitude, company.longitude]]})}
                fill="none"
                stroke="red"
                strokeWidth="0.2"
              ></path>
              <Distillery distillery={d} />
            </React.Fragment>
          )
        })}
      </>
    );
  }
}

export default Company;
