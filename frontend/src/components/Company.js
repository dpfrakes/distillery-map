import React, { Component } from "react";
import Distillery from "./Distillery";
import constants from '../utils/constants';

class Company extends Component {
  constructor(props) {
    super(props);
    this.state = {
      coordinates: [],
      active: false,
      // also track active children to highlight individual connection
      activeDistillery: ''
    };
    this._setActiveDistillery = this._setActiveDistillery.bind(this);
  }

  _setActiveDistillery(activeDistillery) {
    // Callback function to set active distillery on hover
    this.setState({activeDistillery});
  }

  componentDidMount() {
    // Transform coordinates based on projection
    const { company } = this.props;
    const coordinates = constants.projection([company.latitude, company.longitude]);
    this.setState({coordinates});
  }

  render() {
    const { company } = this.props;

    return (
      <>
        <rect
          className="company"
          x={this.state.coordinates[0]}
          y={this.state.coordinates[1]}
          fill={this.state.active ? "blue" : "black"}
          width={`${3 / Math.sqrt(this.props.zoomLevel)}px`}
          height={`${3 / Math.sqrt(this.props.zoomLevel)}px`}
          data-name={company.name}
          onMouseOver={() => { this.setState({active: true}) }}
          onMouseLeave={() => { this.setState({active: false }) }}
          />
        {company.distilleries.map((d, i) => {
          return (
            <React.Fragment key={i}>
              <path
                className="connection"
                d={this.props.path({type: "LineString", coordinates: [[d.latitude, d.longitude], [company.latitude, company.longitude]]})}
                fill="none"
                stroke={(this.state.active || this.state.activeDistillery == d) ? "blue" : "gray"}
                strokeWidth={`${0.2 / Math.sqrt(this.props.zoomLevel)}px`}
              ></path>
              <Distillery distillery={d} hq={company} path={this.props.path} zoomLevel={this.props.zoomLevel} cb={this._setActiveDistillery} />
            </React.Fragment>
          )
        })}
      </>
    );
  }
}

export default Company;
