var React = require('react');
var PropTypes = React.PropTypes;

function Venue(props) {
  return (<li>{props.name}</li>);
}

module.exports = Venue;
