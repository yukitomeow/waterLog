const path = require('path');

module.exports = {
    entry: './App.js',
    output: {
        path: path.resolve('../static/js'),  // Output into Django's static files directory
        filename: 'bundle.js',
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader'],
            },
        ],
    },
    resolve: {
        extensions: ['.js', '.jsx'],
    },
};
