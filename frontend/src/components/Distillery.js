import React, { Component } from "react";

class Distillery extends Component {
  constructor(props) {
    super(props);
    this.state = props;
  }

  componentDidMount() {
    // get events API call
  }

  render() {
    return (
      <div className="distillery"></div>
    );
  }
}

export default Distillery;
