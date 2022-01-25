#!/bin/bash
mkdir -p a/b/c
find . -maxdepth 1 -type d -execdir touch {}/foo \;
#this is a test program to add foo to directories

