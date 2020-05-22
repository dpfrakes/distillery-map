import React, { Component } from "react";

class Tooltip extends Component {

  _formatLocation(lat, lng) {
    if (!!lat && !!lng) {
      const lat_deg = parseInt(lat)
      const lat_min = Math.abs(parseInt((lat % 1) * 60))
      const lat_sec = Math.abs(parseInt((((lat % 1) * 60) % 1) * 60))
      const lng_deg = parseInt(lng)
      const lng_min = Math.abs(parseInt((lng % 1) * 60))
      const lng_sec = Math.abs(parseInt((((lng % 1) * 60) % 1) * 60))
      return `${lat_deg}°${lat_min}\'${lat_sec}" ${lng_deg}°${lng_min}\'${lng_sec}"`
    }
    return "";
  }

  render() {
    const defaultBackground = "https://www.undiscoveredscotland.co.uk/usfeatures/maltwhisky/images-washstill/still18-benromach.jpg";

    if (!this.props.entity) return <></>;

    const info = this.props.entity.info;

    return (
      <div className="tooltip">
        <div className="image" style={{backgroundImage: `url(${info ? info.logo_url || info.image || defaultBackground : defaultBackground})`}}></div>
          {this.props.entity.type == "distillery" ? (
            <div className="entity-info">
              <h2>{info.name}</h2>
              Owner: {info.owner || "--"}<br/>
              Region: {info.region || "--"}<br/>
              Location: {this._formatLocation(info.latitude, info.longitude) || "--"}<br/>
              Est: {info.year_established || "--"}<br/>
            </div>
          ) : (this.props.entity.type == "company" ? (
            <div className="entity-info">
              <h2>{info.name}</h2>
              {info.distilleries.map((d, i) =>
                <React.Fragment key={i}>{d.name}<br/></React.Fragment>
              )}
            </div>
          ) : <></>)}
      </div>
    )
  }

}

export default Tooltip;
