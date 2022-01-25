#!/bin/bash
mkdir -p a/b/c
find . -maxdepth 1 -type d -execdir touch {}/foo \;

