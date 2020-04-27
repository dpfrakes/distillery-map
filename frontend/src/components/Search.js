import React, { Component } from "react";

class Search extends Component {
  constructor(props) {
    super(props);
    this.state = {
      q: '',
      autocomplete: ['glenfarclas', 'glenfiddich', 'glen livet'],
      options: []
    };
    this._handleSubmit = this._handleSubmit.bind(this);
    this._handleType = this._handleType.bind(this);
  }

  componentDidMount() {
    // get events API call
  }

  _handleType(e) {
    let q = e.target.value;
    this.setState({q});
    console.log('get autocomplete results');
    fetch(`/api/distilleries/?search=${q}`)
      .then((data) => data.json())
      .then((json) => console.log(json));
  }

  _handleSubmit(e) {
    e.preventDefault();
    fetch(`/api/distilleries/?search=${this.state.q}`)
      .then((data) => data.json())
      .then((json) => console.log(json));
  }

  render() {
    return (
      <div id="search">

        <form onSubmit={this._handleSubmit}>
          <input type="text" name="q" id="searchbar" defaultValue={this.state.q} onChange={this._handleType} />
        </form>

        <ul id="autocomplete-results">
          {this.state.autocomplete.map((result) => {
            <li>{result}</li>
          })}
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
