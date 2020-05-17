import React, { Component } from "react";

class Tooltip extends Component {

  render() {
    const defaultBackground = "https://www.undiscoveredscotland.co.uk/usfeatures/maltwhisky/images-washstill/still18-benromach.jpg";

    if (!this.props.entity) return <></>;

    const info = this.props.entity.info;

    return this.props.entity.type == "distillery" ? (
      <div className="tooltip" style={{backgroundImage: `url(${info.image || defaultBackground})`}}>
        <div className="entity-info">
          <h2>{info.name}</h2>
          <p>{info.owner}</p>
          <p>{info.region}</p>
          <p>{info.coordinates}</p>
          <p>{info.year_established}</p>
        </div>
      </div>
    ) : (
      this.props.entity.type == "company" ? (
        <div className="tooltip" style={{backgroundImage: `url(${info.image || defaultBackground})`}}>
          <div className="entity-info">
            <h2>{info.name}</h2>
            {info.distilleries.map((d) => d.name).join(", ")}
          </div>
        </div>
      ) : <></>
    )
  }

}

export default Tooltip;
