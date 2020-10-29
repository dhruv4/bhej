#!/usr/bin/env node

var fs = require('fs')
var FormData = require('form-data');
var fetch = require('node-fetch');

console.log("Hello, here is my first CLI tool")

console.log(process.argv)

if (process.argv.length > 3 && process.argv[2] == 'upload') {
  var fileName = process.argv[3];
  var file = fs.readFile(fileName, function (err, data) {
    if (err) throw err;

    console.log(data)
    // console.log(file.name)
    const form = new FormData();
    form.append('file', data, {
      filename: fileName,
    });
    return fetch(`http://localhost:5000/upload`, { method: 'POST', body: form })
  });
}
