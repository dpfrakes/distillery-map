import React, { Component } from "react";

class Tooltip extends Component {
  constructor(props) {
    super(props);
    this.state = {
      distillery: {
        name: "",
        image: "https://via.placeholder.com/350x150"
      },
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
      <div className="tooltip" style={{backgroundImage: `url(${this.state.distillery.image}`}}>
        <div className="distillery-info">
          <h4>{distillery.name || "Distillery"}</h4>
          <p>Lorem ipsum dolor</p>
        </div>
      </div>
    ) : (
      <p>{this.state.placeholder}</p>
    );
  }
}

export default Tooltip;
