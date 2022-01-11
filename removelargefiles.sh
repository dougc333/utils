#!/bin/sh
git filter-branch --tag-name-filter cat --index-filter 'git rm -r --cached --ignore-unmatch kaggle/rossmann/original/train.csv' --prune-empty -f -- --all

