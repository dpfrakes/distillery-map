import React, { Component } from "react";
import { render } from "react-dom";

class Tooltip extends Component {
  constructor(props) {
    super(props);
    this.state = {
      distillery: {},
      loaded: true,
      placeholder: "Loading..."
    };
  }

  componentDidMount() {
    // get events API call
  }

  render() {
    const distillery = this.state.distillery;

    return this.state.loaded ? (
      <div className="tooltip">
        <img src="https://via.placeholder.com/350x150" />
        <div className="distillery-info">
          <p>{distillery.name}</p>
          <p>Lorem ipsum dolor</p>
        </div>
      </div>
    ) : (
      <p>{this.state.placeholder}</p>
    );
  }
}

export default Tooltip;

const container = document.getElementById("cart");
if (container) {
  render(<Cart />, container);
}
