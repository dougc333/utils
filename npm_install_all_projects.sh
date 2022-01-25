#!/bin/bash
 #https://stackoverflow.com/questions/18112204/get-all-directories-within-directory-nodejs
find . -maxdepth 1 -type d -execdir npm install \;

