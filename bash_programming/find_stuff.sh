#!/bin/bash
#this finds directories where this shell is run and goes one level deep to run
#an echo command. {} is the special argument for teh return value of find which in this case is the directory name
find . -type d -maxdepth 1 -mindepth 1  -exec echo {} \;
