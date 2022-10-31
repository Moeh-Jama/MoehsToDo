const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

console.log('PATH', path.resolve(__dirname, 'dist'));
console.log('entry', path.resolve(__dirname, './src/index.tsx'));
module.exports = {
  entry:  './src/index.tsx',
  target: "web",
  mode: "development",
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js', 'json'],
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  plugins: [
    new HtmlWebpackPlugin({
        template: './public/index.html',
        filename: './index.html'
    }),
  ],
};