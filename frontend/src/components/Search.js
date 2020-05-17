import React, { Component } from "react";

class Search extends Component {
  constructor(props) {
    super(props);
    this.state = {
      q: '',
      sidebarOpen: true,
      autocomplete: {},
      options: []
    };

    this._handleType = this._handleType.bind(this);
    this._onSelect = this._onSelect.bind(this);
  }

  componentDidMount() {
    // get events API call
  }

  _handleType(e) {
    let q = e.target.value;
    let autocomplete = {};

    if (q) {
      const matchingDistilleries = this.props.distilleries.filter((d) => d.name.toLowerCase().indexOf(q.toLowerCase()) >= 0);
      if (matchingDistilleries.length > 0) {
        autocomplete['distilleries'] = matchingDistilleries;
      }

      const matchingCompanies = this.props.companies.filter((c) => c.name.toLowerCase().indexOf(q.toLowerCase()) >= 0);
      if (matchingCompanies.length > 0) {
        autocomplete['companies'] = matchingCompanies;
      }
    }
    this.setState({q, autocomplete});
  }

  _onSelect(e) {
    // Complete query string and clear autocomplete results
    this.setState({
      q: e.target.innerText,
      autocomplete: {}
    });

    // Notify BaseMap component of active entity (and its type) via callback fn
    if (this.props.onSelect) {
      const entitySection = e.target.getAttribute('data-entity-section');
      this.props.onSelect(entitySection, e.target.innerText);
    }
  }

  render() {
    return (
      <div id="sidebar" className={this.state.sidebarOpen ? "open" : ""}>

        <form onSubmit={(e) => e.preventDefault()}>
          <input type="text" name="q" id="search" autoComplete="off" value={this.state.q} onChange={this._handleType} />
        </form>

        {Object.keys(this.state.autocomplete).length ? (
          <ul id="autocomplete-results">
            {Object.keys(this.state.autocomplete).map((a, i) =>
              <React.Fragment key={i}>
                <div className="autocomplete-section">{a}</div>
                {this.state.autocomplete[a].map((b, j) =>
                  <li key={j} onClick={this._onSelect} data-entity-section={a}>{b.name}</li>
                )}
              </React.Fragment>
            )}
          </ul>
        ) : <></>}

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
