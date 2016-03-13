var React = require('react');
var ReactDOM = require('react-dom');
var axios = require('axios');

var SearchTool = React.createClass({
  getInitialState: function() {
    return {
      address: '',
      lat: null,
      lng: null,
      venues: []
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
      }.bind(this))
      .catch(function (response) {
        console.log(response);
      });
  },
  getVenues: function() {
    return axios.get('/suggest/ajax/find_venues/' + this.state.lat + ',' + this.state.lng + '/')
      .then(function (response) {
        console.log("Got venues", response);
        this.setState({venues: response.data});
      }.bind(this))
      .catch(function (response) {
        console.log(response);
      });
  },
  onSubmitAddress: function(e) {
    e.preventDefault();
    this.getFullAddress()
      .then(this.getVenues);
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
        <Results data={this.state.venues} />
      </div>
    );
  }
});

function Results(props) {
  var list = props.data.reduce(function(accumultor, item) {
    accumultor += <li>{item.name}</li>;
  }, "");
  return (
    <ul>
      {list}
    </ul>
  );
}

ReactDOM.render(<SearchTool />, document.getElementById('main'));
