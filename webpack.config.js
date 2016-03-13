var HTMLWebpackPlugin = require("html-webpack-plugin");
var HTMLWebpackPluginConfig = new HTMLWebpackPlugin({
  template: __dirname + "/templates/home3.html",
  filename: "index.html",
  inject: "body"
});

module.exports = {
  entry: [
    './js-src/index.js'
  ],
  module: {
    loaders: [
      {test: /\.js$/, exclude: /node_modules/, loader: "babel-loader", query: {
          presets: ['react']
        }
      }
    ]
  },
  output: {
    filename: "index_bundle.js",
    path: __dirname + "/js"
  },
  plugins: [HTMLWebpackPluginConfig]
}
