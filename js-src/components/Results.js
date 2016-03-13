var React = require('react');
var PropTypes = React.PropTypes;
var Venue = require('./Venue');

function Results(props) {
  return (
    <ul>
      {props.data.map(function(item) {
        return <Venue key={item.pk} name={item.fields.name} />
      })}
    </ul>
  );
}

module.exports = Results;
