var React = require('react');
var axios = require('axios');
var PropTypes = React.PropTypes;
var Results = require('./Results');

var SearchTool = React.createClass({
  getInitialState: function() {
    return {
      address: '',
      lat: null,
      lng: null,
      venues: [],
      error: ''
    };
  },
  onAddressChange: function(e) {
    this.setState({
      address: e.target.value
    });
  },
  getFullAddress: function() {
    return axios.get('/suggest/ajax/lat_lng/' + this.state.address)
      .then(function (response) {
        this.setState({
          address: response.data.address,
          lat: response.data.lat,
          lng: response.data.lng
        });
      }.bind(this));
  },
  getVenues: function() {
    return axios.get('/suggest/ajax/find_venues/' + this.state.lat + ',' + this.state.lng + '/')
      .then(function (response) {
        this.setState({venues: response.data, error: ''});
      }.bind(this));
  },
  onSubmitAddress: function(e) {
    e.preventDefault();
    this.getFullAddress()
      .then(this.getVenues)
      .catch(function (response) {
        this.setState({venues: [], error: "Couldn't find address. Please try again."})
        console.log(response);
      }.bind(this));
  },
  render: function() {
    return (
      <div>
        <form>
          Find venues that have shown unusual films around
          <input type="text" value={this.state.address} placeholder="Your location" onChange={this.onAddressChange} />
          <p>
            <button type="submit" onClick={this.onSubmitAddress}>Show Me</button>
          </p>
        </form>
        {this.state.error}
        <Results data={this.state.venues} />
      </div>
    );
  }
});

module.exports = SearchTool;
