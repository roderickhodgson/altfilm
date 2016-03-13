var React = require('react');
var ReactDOM = require('react-dom');
var axios = require('axios');

var SearchTool = React.createClass({
  getInitialState: function() {
    return {
      address: '',
      lat: null,
      lng: null
    };
  },
  onAddressChange: function(e) {
    this.setState({
      address: e.target.value
    });
  },
  onSubmitAddress: function(e) {
    e.preventDefault();
    axios.get('/suggest/ajax/lat_lng/' + this.state.address)
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
        <Results />
      </div>
    );
  }
});

function Results(props) {
  return (
    <ul>
    </ul>
  );
}

ReactDOM.render(<SearchTool />, document.getElementById('main'));
