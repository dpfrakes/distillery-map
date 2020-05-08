import React, { Component } from "react";

class Tooltip extends Component {
  render() {
    const defaultBackground = "https://www.undiscoveredscotland.co.uk/usfeatures/maltwhisky/images-washstill/still18-benromach.jpg";

    return this.props.distillery ? (
      <div className="tooltip" style={{backgroundImage: `url(${this.props.distillery.image || defaultBackground})`}}>
        <div className="distillery-info">
          <h2>{this.props.distillery.name}</h2>
          <p>{this.props.distillery.region}</p>
          <p>{this.props.distillery.coordinates}</p>
          <p>{this.props.distillery.year_established}</p>
        </div>
      </div>
    ) : (
      <></>
    );
  }
}

export default Tooltip;
