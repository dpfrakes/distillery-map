import React, { Component } from "react";

class Search extends Component {
  constructor(props) {
    super(props);
    this.state = {
      q: '',
      autocomplete: [],
      options: []
    };
    this._handleSubmit = this._handleSubmit.bind(this);
    this._handleType = this._handleType.bind(this);
    this._focusDistillery = this._focusDistillery.bind(this);
  }

  componentDidMount() {
    // get events API call
  }

  _handleType(e) {
    let q = e.target.value;
    this.setState({q});
    if (q) {
      // TODO replace with react search
      fetch(`/api/distilleries/?search=${q}`)
        .then((data) => data.json())
        .then((json) => {
          this.setState({autocomplete: json.results.map((d) => d.name)});
        });
    } else {
      this.setState({autocomplete: []});
    }
  }

  _handleSubmit(e) {
    e.preventDefault();
    fetch(`/api/distilleries/?search=${this.state.q}`)
      .then((data) => data.json())
      .then((json) => console.log(json));
  }

  _focusDistillery(e) {
    this.setState({
      q: e.target.innerText,
      autocomplete: []
    });
  }

  render() {
    return (
      <div id="search">

        <form onSubmit={this._handleSubmit}>
          <input type="text" name="q" id="searchbar" autoComplete="off" value={this.state.q} onChange={this._handleType} />
        </form>

        <ul id="autocomplete-results">
          {this.state.autocomplete.map((result, i) =>
            <li key={i} onClick={this._focusDistillery}>{result}</li>
          )}
        </ul>

        <ul id="options">
          {this.state.options.map((opt) => {
            <li>{opt}</li>
          })}
        </ul>

    </div>
    );
  }
}

export default Search;
