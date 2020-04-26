import React, { Component } from "react";

class Tooltip extends Component {
  render() {
    return this.props.distillery ? (
      <div className="tooltip" style={{backgroundImage: `url(${this.props.distillery.image || "https://via.placeholder.com/350x150"})`}}>
        <div className="distillery-info">
          <h4>{this.props.distillery.name}</h4>
          <p>Lorem ipsum dolor</p>
        </div>
      </div>
    ) : (
      <></>
    );
  }
}

export default Tooltip;
