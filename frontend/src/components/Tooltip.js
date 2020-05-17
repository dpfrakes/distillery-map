import React, { Component } from "react";

class Tooltip extends Component {

  render() {
    const defaultBackground = "https://www.undiscoveredscotland.co.uk/usfeatures/maltwhisky/images-washstill/still18-benromach.jpg";
    if (this.props.company) console.log(this.props.company);

    return !!this.props.distillery ? (
      <div className="tooltip" style={{backgroundImage: `url(${this.props.distillery.image || defaultBackground})`}}>
        <div className="entity-info">
          <h2>{this.props.distillery.name}</h2>
          <p>{this.props.distillery.owner}</p>
          <p>{this.props.distillery.region}</p>
          <p>{this.props.distillery.coordinates}</p>
          <p>{this.props.distillery.year_established}</p>
        </div>
      </div>
    ) : (
      !!this.props.company ? (
        <div className="tooltip" style={{backgroundImage: `url(${this.props.company.image || defaultBackground})`}}>
          <div className="entity-info">
            <h2>{this.props.company.name}</h2>
            {this.props.company.distilleries.map((d) => d.name).join(", ")}
          </div>
        </div>
      ) : <></>
    )
  }

}

export default Tooltip;
