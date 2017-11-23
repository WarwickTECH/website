/**
 * Configuration file for webpack.
 */


// Dependencies.
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

// Set up module.

module.exports = {

  // Base directory for resolving the entry option.
  context: path.resolve(__dirname, "../../../"),

  entry: './warwick_tech/static/registration/assets/js/index.js',

  output: {
    path: path.resolve(__dirname, "./assets/bundles/"),
    filename: '[name]-[hash].js'
  },

  plugins: [
    // Stores data about the bundle being generated.
    new BundleTracker({filename: './webpack-stats.json'}),

    // Import jQuery as a plugin.
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery'
    })
  ],

  module: {
    // Loaders pre-process given module files which we require, such as babel,
    // for jsx preprocessing.
    loaders: [
       {
         // Only pre-process .js & .jsx files in our loader(s).
         test: /\.jsx?$/,

         // Do not pre-process all of node_modules (unnecessary).
         exclude: path.resolve(__dirname, "../../../../node_modules"),

         // Specify babel transpiler.
         loader: 'babel-loader',

         // Use query preset for React.
         query: {
           presets: ['react']
         }
       }
    ]
  },

  resolve: {
    // Specify where webpack should look to resolve modules.
    modules: ['node_modules'],

    // File types specified for resolving modules.
    extensions: ['.js', '.jsx']
  }

}
