import React, { Component } from "react";

class Search extends Component {
  constructor(props) {
    super(props);
    this.state = {
      q: '',
      autocomplete: ['glenfarclas', 'glenfiddich', 'glen livet'],
      options: []
    };
  }

  componentDidMount() {
    // get events API call
  }

  render() {
    return (
      <div id="search">

        <form action="/search/" method="POST">
          <input type="text" name="q" id="searchbar" defaultValue={this.state.q} />
          <input type="submit" />
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
