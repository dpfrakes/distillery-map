import React, { Component } from "react";

class Distillery extends Component {
  constructor(props) {
    super(props);
    this.state = {
      marker: {}
    };

    this.showTooltip = this.showTooltip.bind(this);
  }

  showTooltip(distillery) {
    console.log('populate tooltip this this info:');
    console.log(distillery);
  }

  hideTooltip() {
    console.log('hide tooltip!');
  }

  componentDidMount() {
    // get events API call
  }

  render() {
    return (
      <circle
        className="distillery"
        cx={this.state.marker.x}
        cy={this.state.marker.y}
        r={this.state.marker.r}
        fill={this.state.marker.fill}
        data-name={this.props.name}
        data-region={this.props.region}
        data-year-est={this.props.yearEst}
        onClick={() => { console.log(this) }}
      >
      </circle>
    );
  }
}

export default Distillery;
