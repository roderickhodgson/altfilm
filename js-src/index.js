var React = require('react');
var ReactDOM = require('react-dom');

var React = require('react');
var PropTypes = React.PropTypes;

var Test = React.createClass({

  propTypes: {

  },
  getInitialState: function() {
    return {

    }
  },
  render: function() {
    return (
      <div>Test</div>
    );
  }

});

ReactDOM.render(<Test />, document.getElementById('main'));
